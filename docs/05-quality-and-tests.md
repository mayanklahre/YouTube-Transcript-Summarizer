# Quality and tests

## Current evidence
- **12 pytest tests** are present in the repository.
- Input validation and controlled 400, 404, and 502 error responses are implemented.
- Local API setup, test command, and Chrome extension loading are documented.
- The transcript is tokenised and chunked at 900 tokens to respect the 1,024-token model input limit.

## Manual quality checks
1. Start the local Flask API.
2. Load the unpacked extension in Chrome.
3. Test an eligible YouTube video with an English transcript.
4. Test invalid/non-YouTube URL and missing-transcript behaviour.
5. Test a long transcript and inspect whether combined output remains useful.
6. Re-run pytest after dependency upgrades and test extension/API communication.

## Quality limits
The app supports English transcripts only, is not Chrome Web Store published, and runs locally. Summaries are generative and should be treated as an overview, not a verified substitute for the transcript.
