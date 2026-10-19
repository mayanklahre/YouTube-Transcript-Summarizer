# Risks and mitigations

| Risk | Impact | Mitigation | Residual limit |
| --- | --- | --- | --- |
| No English transcript | User cannot obtain a summary | State English-only limitation and return controlled error. | Coverage depends on YouTube transcript availability. |
| Dependency changes break application | Medium | Pin compatible versions, keep requirements current, run tests after upgrades. | Upstream libraries can still change or deprecate behaviour. |
| Very long transcript creates fragmented output | Medium | Use chunking and document the limitation. | Combined result may read as a list of points. |
| Model download/local resource cost | Medium | Document first-run download and local-only runtime expectation. | User machine capability affects responsiveness. |
| Hallucinated/incomplete summary | Medium | Frame output as an aid; retain source-video context; do not use it as authoritative transcript replacement. | Generative summaries can omit or distort detail. |
| Extension/API mismatch | Medium | Maintain an end-to-end manual check and extension loading guidance. | Browser/platform changes may require maintenance. |
