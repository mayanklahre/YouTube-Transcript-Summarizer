# Decision log

| ID | Decision | Options considered | Choice and rationale | Consequence |
| --- | --- | --- | --- | --- |
| D-01 | Service architecture | Browser-only processing; hosted API; local Flask API | **Local Flask API** keeps model execution and transcript handling on the user’s machine for the project scope. | Users must install dependencies and run the API locally. |
| D-02 | Summarisation model | Extractive approach; larger hosted model; DistilBART | **sshleifer/distilbart-cnn-12-6** offers an available abstractive summarisation path usable in the local prototype. | First use may require model download; quality can vary by transcript. |
| D-03 | Chunk size | Whole transcript; maximum-sized chunks; 900-token chunks | **900-token chunks** stay below the model’s 1,024-token input limit with operational headroom. | Very long-video output can read as separate points rather than one cohesive summary. |
| D-04 | Extension approach | Older manifest; web application only; Manifest V3 | **Chrome Manifest V3** supports the extension workflow used in the repository. | Project is local and not Web Store published. |
| D-05 | Dependency management | Floating versions; pinned compatible versions | **Pinned compatible dependencies** after two library changes broke the app, to improve reproducibility. | Dependencies still require periodic review and upgrade testing. |
