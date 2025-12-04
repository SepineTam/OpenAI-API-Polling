# OpenAI-API-Polling

Polling OpenAI API without rate limit issues.

## Quickly Start

You can use `pip` to install this package.

```bash
pip install openai-api-polling
```

A simple example:
```python
from openai_api_polling.polling import ClientPolling

api_keys = [
    "<your api key a>", 
    "<your api key> b",
    "<your api key> c",
]
client_polling = ClientPolling(api_keys=api_keys)

for _ in range(10):
    resp = client_polling.client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello! Explain the core of Game Theory."},
        ]
    )
    print(resp.choices[0].message.content)
```

