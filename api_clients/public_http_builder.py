from httpx import Client

from api_clients.event_hooks import curl_event_hook, log_request_event_hook, log_response_event_hook
from config import settings
from utils.api.fiddler_check import is_fiddler_running

use_proxy = is_fiddler_running()
proxy_url = settings.http_client.proxy if use_proxy else None


def get_public_http_client() -> Client:
    return Client(
        base_url=settings.http_client.client_url,
        timeout=settings.http_client.timeout,
        proxy=proxy_url if use_proxy else None,
        verify=False if use_proxy else True,
        event_hooks={
            "request": [curl_event_hook, log_request_event_hook],
            "response": [log_response_event_hook]
        }
    )


