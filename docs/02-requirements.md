# Requirements and acceptance criteria

| ID | User story | Acceptance criteria |
| --- | --- | --- |
| RQ-01 | As a viewer, I can request a summary for the current YouTube video. | The extension sends the active YouTube URL to the local API and displays returned summary/error state. |
| RQ-02 | As a viewer, I can summarise an eligible English transcript. | The API extracts the video identifier, retrieves the transcript, and returns a text summary as JSON. |
| RQ-03 | As a maintainer, I can avoid exceeding the model input limit. | Tokenised transcript input is split into 900-token chunks against the model’s 1,024-token limit; chunk summaries are combined. |
| RQ-04 | As a user, I receive clear failures. | Invalid input, missing/unavailable transcript, and upstream failures return controlled 400, 404, or 502 responses. |
| RQ-05 | As a maintainer, I can reproduce the local workflow. | Requirements, extension loading instructions, API command, and pytest command are documented. |
| RQ-06 | As a reviewer, I understand provenance. | README/docs disclose local-only status, English-only limit, AI assistance for improved implementation, and any confirmed tutorial attribution. |
