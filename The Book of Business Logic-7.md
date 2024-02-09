# API Key Authentication in FastAPI: A Main.py Only Implementation

Implementing API Key Authentication in FastAPI using a "main.py only" paradigm is straightforward and suits projects where simplicity and minimal external dependencies are preferred. Here's a real-world example that you can cut and paste into your `main.py` file to add API Key Authentication to your FastAPI application:

```python
from fastapi import FastAPI, Security, Depends, HTTPException, status
from fastapi.security.api_key import APIKeyHeader, APIKey
from typing import List

app = FastAPI()

API_KEY = "your_secret_api_key_here"
API_KEY_NAME = "access_token"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=True)

async def get_api_key(api_key: str = Security(api_key_header)):
    if api_key == API_KEY:
        return api_key
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Could not validate API Key"
        )

@app.get("/items/", dependencies=[Depends(get_api_key)])
async def read_items():
    return [{"item": "Foo", "value": "Bar"}]

@app.get("/secure-data/", dependencies=[Depends(get_api_key)])
async def read_secure_data():
    return {"secure_data": "Sensitive info accessible only with a valid API key."}
```

### Explanation:
- **API Key Setup**: This example uses a simple string (`API_KEY`) as the API key. In a real-world scenario, you'd generate a secure key and possibly manage multiple keys depending on your needs.
- **API Key Header**: The `APIKeyHeader` class is used to extract the API key from the request headers. The key name (`access_token`) must match what the client will send.
- **Security Dependency**: The `get_api_key` function is a dependency that validates the API key. If the key is incorrect or missing, it raises an HTTP 403 Forbidden error.
- **Protecting Routes**: Routes are protected by adding a `dependencies` parameter to the route decorator, which includes the `Depends(get_api_key)` dependency. This setup ensures that the API key is validated for each request to these endpoints.

### How to Test:
1. Start your FastAPI application.
2. Use a tool like `curl` or Postman to make requests to the protected endpoints.
3. Include the API key in the request headers: `"access_token: your_secret_api_key_here"`.

```bash
curl -H "access_token: your_secret_api_key_here" http://localhost:8000/items/
```

If the API key matches, you'll get access to the protected resources. If not, you'll receive a 403 Forbidden response.

This "main.py only" approach keeps the application simple and manageable without the need for extensive directory structures or dependency management, ideal for smaller projects or for those preferring a minimalistic setup.