import pytest
from youtube_transcript_api import TranscriptsDisabled

import app as appmod


@pytest.fixture
def client():
    return appmod.app.test_client()


@pytest.mark.parametrize(
    "url,expected",
    [
        ("https://www.youtube.com/watch?v=dQw4w9WgXcQ", "dQw4w9WgXcQ"),
        ("https://www.youtube.com/watch?feature=share&v=dQw4w9WgXcQ", "dQw4w9WgXcQ"),
        ("https://www.youtube.com/watch?v=dQw4w9WgXcQ&t=30s", "dQw4w9WgXcQ"),
        ("https://youtu.be/dQw4w9WgXcQ", "dQw4w9WgXcQ"),
        ("https://www.youtube.com/shorts/dQw4w9WgXcQ", "dQw4w9WgXcQ"),
        ("https://www.youtube.com/", None),
        ("https://example.com/watch?v=dQw4w9WgXcQ", None),
        ("", None),
    ],
)
def test_extract_video_id(url, expected):
    assert appmod.extract_video_id(url) == expected


def test_split_into_chunks():
    assert appmod.split_into_chunks(list(range(5)), size=2) == [[0, 1], [2, 3], [4]]
    assert appmod.split_into_chunks([], size=2) == []


def test_rejects_bad_url(client):
    response = client.get("/summary?url=https://www.youtube.com/")
    assert response.status_code == 400
    assert "error" in response.get_json()


def test_no_transcript_returns_404(client, monkeypatch):
    def raise_disabled(video_id):
        raise TranscriptsDisabled(video_id)

    monkeypatch.setattr(appmod, "get_transcript", raise_disabled)
    response = client.get("/summary?url=https://youtu.be/dQw4w9WgXcQ")
    assert response.status_code == 404


def test_success_returns_summary(client, monkeypatch):
    monkeypatch.setattr(appmod, "get_transcript", lambda video_id: "some long transcript")
    monkeypatch.setattr(appmod, "summarise", lambda text: "short summary")
    response = client.get("/summary?url=https://youtu.be/dQw4w9WgXcQ")
    assert response.status_code == 200
    assert response.get_json() == {"summary": "short summary"}
