import re
from functools import lru_cache
from urllib.parse import parse_qs, urlparse

from flask import Flask, jsonify, request
from youtube_transcript_api import (
    NoTranscriptFound,
    TranscriptsDisabled,
    VideoUnavailable,
    YouTubeTranscriptApi,
    YouTubeTranscriptApiException,
)

MODEL_NAME = "sshleifer/distilbart-cnn-12-6"
CHUNK_TOKENS = 900  # the model accepts at most 1024 input tokens
MAX_SUMMARY_TOKENS = 150
MIN_SUMMARY_TOKENS = 30

app = Flask(__name__)


def extract_video_id(url):
    """Return the 11-character video id from a watch, youtu.be, shorts or embed URL, else None."""
    parsed = urlparse(url)
    host = (parsed.hostname or "").lower().removeprefix("www.")
    candidate = None
    if host == "youtu.be":
        candidate = parsed.path.lstrip("/").split("/")[0]
    elif host in ("youtube.com", "m.youtube.com", "music.youtube.com"):
        if parsed.path == "/watch":
            candidate = parse_qs(parsed.query).get("v", [None])[0]
        else:
            parts = parsed.path.strip("/").split("/")
            if len(parts) >= 2 and parts[0] in ("shorts", "embed", "live", "v"):
                candidate = parts[1]
    if candidate and re.fullmatch(r"[A-Za-z0-9_-]{11}", candidate):
        return candidate
    return None


def get_transcript(video_id):
    snippets = YouTubeTranscriptApi().fetch(video_id)
    return " ".join(snippet.text for snippet in snippets)


@lru_cache(maxsize=1)
def load_model():
    """Load the tokenizer and model once, on the first request, and reuse them."""
    from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
    model.eval()
    return tokenizer, model


def split_into_chunks(token_ids, size=CHUNK_TOKENS):
    return [token_ids[i:i + size] for i in range(0, len(token_ids), size)]


def summarise(text):
    """Summarise long text by splitting it into token-sized chunks and summarising each one."""
    import torch

    tokenizer, model = load_model()
    token_ids = tokenizer(text, add_special_tokens=False)["input_ids"]
    parts = []
    for chunk in split_into_chunks(token_ids):
        chunk_text = tokenizer.decode(chunk, skip_special_tokens=True)
        inputs = tokenizer(chunk_text, return_tensors="pt", truncation=True, max_length=1024)
        max_len = min(MAX_SUMMARY_TOKENS, max(16, len(chunk) // 2))
        min_len = min(MIN_SUMMARY_TOKENS, max_len // 2)
        with torch.no_grad():
            output = model.generate(
                **inputs,
                max_length=max_len,
                min_length=min_len,
                num_beams=4,
                early_stopping=True,
            )
        parts.append(tokenizer.decode(output[0], skip_special_tokens=True))
    return " ".join(parts)


@app.get("/summary")
def summary_api():
    video_id = extract_video_id(request.args.get("url", ""))
    if not video_id:
        return jsonify(error="Open a YouTube video page and try again."), 400
    try:
        transcript = get_transcript(video_id)
    except (TranscriptsDisabled, NoTranscriptFound):
        return jsonify(error="This video has no English transcript available."), 404
    except VideoUnavailable:
        return jsonify(error="This video is unavailable."), 404
    except YouTubeTranscriptApiException:
        return jsonify(error="Could not fetch the transcript from YouTube."), 502
    if not transcript.strip():
        return jsonify(error="The transcript is empty."), 404
    return jsonify(summary=summarise(transcript)), 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
