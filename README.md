# YouTube Transcript Summarizer

**Solo project | Local Chrome Extension and Flask API | Improved implementation developed with AI assistance**

## Problem
A viewer may want a shorter overview of a YouTube video with an available English transcript. Reading a long transcript manually is slow, and the project demonstrates a local extension-to-API summarisation workflow.

## Who it is for
A user who can run a local Flask API and load an unpacked Chrome extension. The extension is not published to the Chrome Web Store.

## Goal and success criteria
Retrieve an eligible English transcript, keep model input below its 1,024-token limit, generate an abstractive summary, and surface clear errors. The implementation uses 900-token chunks and combines chunk summaries.

## Scope
**In:** Chrome Manifest V3 extension, local Flask API, English transcript retrieval, DistilBART summarisation, 900-token chunking, validation, controlled errors, and tests.

**Out:** non-English/no-transcript videos, hosted service, Chrome Web Store publishing, guaranteed factual completeness, and long-form multilingual transcription.

## Key decisions
- Local Flask API keeps the project’s model processing on the user’s machine.
- DistilBART provides an abstractive-summarisation baseline.
- 900-token chunks operate within the model’s 1,024-token input limit.
- Compatible dependency versions are pinned following an incident in which two library changes broke the app.

See the [decision log](docs/03-decision-log.md).

## Outcome
The repository includes a local extension/API workflow, controlled HTTP errors, **12 pytest tests**, and setup documentation. It is functional locally but does not claim a hosted or Chrome Web Store release.

## Risks and mitigations
The main limits are English-transcript availability, dependency changes, model-resource needs, output fragmentation for long videos, and generative-summary accuracy. See [risks](docs/04-risks.md).

## How to run
    pip install -r requirements.txt
    python app.py

The first request downloads the model. In Chrome, open chrome://extensions, enable Developer mode, choose Load unpacked, and select this repository folder. Open an eligible YouTube video with English captions and click the extension.

Run tests with:

    pip install pytest
    pytest

## Next steps
- Add a demo GIF using a video/transcript you have the right to show.
- Record summary-quality examples and explicit evaluation criteria.
- Test dependency upgrades through CI.
- Add a confirmed tutorial credit if a tutorial was directly adapted; none is guessed or invented.

## Documentation
- [Brief](docs/01-brief.md)
- [Requirements](docs/02-requirements.md)
- [Decision log](docs/03-decision-log.md)
- [Risks](docs/04-risks.md)
- [Quality and tests](docs/05-quality-and-tests.md)
- [Retrospective](docs/06-retrospective.md)
