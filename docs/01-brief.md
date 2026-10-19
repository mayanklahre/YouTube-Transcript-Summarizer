# Project brief

**Project:** YouTube Transcript Summarizer  
**Delivery:** Solo local application and Chrome Extension. Parts of the improved implementation were developed with AI assistance.

## Problem and users
A viewer with a YouTube video that has an English transcript may want a shorter textual overview without manually reading the full transcript. The intended user runs the local extension/API; it is not a published Chrome Web Store product.

## Goal and success criteria
Retrieve a video transcript, split input safely for the summarisation model, generate a readable summary, and surface clear errors when transcript or upstream access is unavailable. The model input is limited to 1,024 tokens, so the application uses 900-token chunks.

## Scope
**In:** Manifest V3 extension, local Flask API, English-transcript retrieval, DistilBART summarisation, input validation, controlled HTTP errors, and tests.

**Out:** videos without English transcripts, a hosted/multi-user service, Chrome Web Store publishing, guaranteed factual accuracy, and a full multilingual transcription platform.
