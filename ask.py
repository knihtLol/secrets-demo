import os
import sys

from openai import OpenAI

# The key is never written in this file. It comes from the environment,
# and in the pipeline GitHub fills it in from the repo secret.
key = os.environ.get("GEMINI_API_KEY")
if not key:
    sys.exit("GEMINI_API_KEY is empty. Is the secret name the same in the YAML and in repo settings?")

# Google offers an OpenAI-compatible endpoint, so we use the OpenAI SDK with Google's address.
client = OpenAI(
    api_key=key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    timeout=30,
    max_retries=1,
)

response = client.chat.completions.create(
    model="gemini-3.5-flash-lite",
    messages=[
        {"role": "user", "content": "In one sentence, why should API keys never be committed to git?"}
    ],
)

print(response.choices[0].message.content)
