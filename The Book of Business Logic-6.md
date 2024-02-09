# Implementing Full-Stack API Key Authentication in FastAPI with Postgres Database

An alternative to OAuth2 for securing a FastAPI application is using API Key authentication. This simpler method can effectively control access to the API, suitable for scenarios where client applications need to access the server resources without a user context. Here's how to implement API Key authentication in a FastAPI application integrated with a Postgres database.

## Database Setup
No changes are required in the database schema for API Key authentication. User identification can still rely on the existing users table.

## FastAPI Security Configuration
FastAPI provides utilities to facilitate API Key authentication. The key can be sent in headers, query parameters, or cookies. For this example, we'll use a header-based approach.

## Implementing API Key Authentication
1. **Define the API Key Header**: Create a custom dependency that extracts the API Key from the request headers.

```python
from fastapi import Depends, FastAPI, HTTPException, Security
from fastapi.security.api_key import APIKeyHeader, APIKey

API_KEY = "your_actual_api_key"
API_KEY_NAME = "access_token"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

async def get_api_key(api_key: str = Security(api_key_header)):
    if api_key == API_KEY:
        return api_key
    else:
        raise HTTPException(status_code=403, detail="Could not validate credentials")
```

2. **Protect Routes with the API Key**: Use the custom dependency to protect specific routes or the entire application.

```python
app = FastAPI()

@app.get("/items/", dependencies=[Depends(get_api_key)])
def read_items():
    return [{"item": "Foo", "value": "Bar"}]
```

## Frontend Integration
For client applications, ensure the API Key is included in the request headers when calling protected endpoints.

## OpenAPI Documentation
While FastAPI's automatic OpenAPI documentation generation doesn't natively support API Key authentication, you can manually document the requirement for an API Key in your route descriptions.

## Implementation Considerations
- API Key authentication does not provide the same level of security as OAuth2, especially in multi-user applications.
- API Keys should be securely stored and transmitted, using HTTPS to protect them in transit.
- Consider rate limiting and monitoring to prevent abuse of endpoints protected by API Key authentication.

Implementing API Key authentication provides a straightforward method for securing FastAPI applications, especially for server-to-server communication or simple client applications. It requires careful management of the API Keys to ensure the security of the application's data and functionality.