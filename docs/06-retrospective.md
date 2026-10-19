# Retrospective

**Retrospective documentation, written on 19 October 2026.** This record reflects the completed solo project and does not claim contemporaneous tracking.

## What worked
- The extension plus local API made the workflow easy to demonstrate without hosting.
- Chunking made long transcripts compatible with the model limit.
- Tests and explicit HTTP errors improved maintainability.

## What was difficult
- Two library changes broke the application during development. The remedy was to identify compatible versions, update the implementation, and pin dependencies so setup is more repeatable.
- Very long transcripts still make a single cohesive summary difficult.
- Transcript availability and language support are external constraints.

## AI assistance and attribution
The improved app.py and popup.js were developed with AI assistance. The project must credit any tutorial directly adapted from once its source is confirmed; no tutorial attribution is invented in this repository.

## Improvements
- Add a rights-cleared demo GIF.
- Add evaluation examples comparing summary completeness to selected transcripts.
- Add a transcript-language selection path if requirements and model support are validated.
- Test dependency upgrades in a repeatable CI workflow.
