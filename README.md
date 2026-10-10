# YouTube Transcript Summarizer

A Chrome extension (Manifest V3) plus a small Flask API that summarizes a YouTube video from its transcript.

## How it works
1. The extension sends the current tab's URL to the local API (`GET /summary?url=...`).
2. The API extracts the video id and fetches the transcript with `youtube-transcript-api`.
3. The transcript is tokenized and split into 900-token chunks (the model accepts at most 1,024 input tokens).
4. Each chunk is summarized with `sshleifer/distilbart-cnn-12-6` (a distilled BART model from Hugging Face), and the chunk summaries are joined into one summary, returned as JSON.

## Run it
```bash
pip install -r requirements.txt
python app.py          # starts the API on http://127.0.0.1:5000 (the model downloads on the first request)
```
Then open `chrome://extensions`, enable Developer mode, choose "Load unpacked", and select this folder.
Open any YouTube video that has English captions and click the extension icon.

## Test
```bash
pip install pytest
pytest
```

## Limitations
- Only videos with an English transcript are supported.
- Summaries are generated per chunk, so very long videos can read as a list of separate points.
- The API runs locally only; the extension is not published to the Chrome Web Store.
