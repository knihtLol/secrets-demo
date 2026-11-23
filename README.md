# secrets-demo

Demo for my CI/CD talk: model API keys in pipelines.

- `ask.py` calls the Gemini API and reads the key from the `GEMINI_API_KEY` environment variable.
- `.github/workflows/call-model.yml` passes the key in from a GitHub Actions secret.
- The key is never in this repo. Run locally with `export GEMINI_API_KEY=...` then `python ask.py`.
