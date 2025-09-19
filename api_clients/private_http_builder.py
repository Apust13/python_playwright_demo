from functools import lru_cache

from httpx import Client

from api_clients.authentication.authentication_client import get_authentication_client
from api_clients.authentication.authentication_schema import AuthenticationUserSchema
from api_clients.event_hooks import curl_event_hook, log_request_event_hook, log_response_event_hook
from api_clients.users.users_schema import LoginRequestSchema
from config import settings
from utils.api.fiddler_check import is_fiddler_running

use_proxy = is_fiddler_running()
proxy_url = settings.http_client.proxy if use_proxy else None


@lru_cache(maxsize=None)
def get_private_http_client(user: AuthenticationUserSchema) -> Client:
    authentication_client = get_authentication_client()
    login_request = LoginRequestSchema(email=user.email, password=user.password)
    login_response = authentication_client.login_api(login_request)

    if login_response.status_code not in [302, 200]:
        raise RuntimeError(f"Login failed: {login_response.status_code}")

    cookies = authentication_client.client.cookies

    return Client(
        base_url=settings.http_client.client_url,
        timeout=settings.http_client.timeout,
        cookies=cookies,
        proxy=proxy_url if use_proxy else None,
        verify=False if use_proxy else True,
        event_hooks={
            "request": [curl_event_hook, log_request_event_hook],
            "response": [log_response_event_hook]
        }
    )