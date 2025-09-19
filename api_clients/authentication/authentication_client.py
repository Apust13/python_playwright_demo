import allure
from httpx import Response

from api_clients.api_client import APIClient
from api_clients.users.users_schema import LoginRequestSchema
from api_clients.public_http_builder import get_public_http_client
from config import settings
from utils.api_routes import ApiRoute


class AuthenticationClient(APIClient):

    @allure.step("Login user {request}")
    def login_api(self, request: LoginRequestSchema) -> Response:
        # headers = {"Referer": "https://automationexercise.com/login"}
        headers = {"Referer": f'{settings.http_client.client_url}{ApiRoute.LOGIN}'}
        request.token = self.get_token()
        return self.post(ApiRoute.LOGIN, data=request.model_dump(by_alias=True), headers=headers)

    @allure.step("Get token")
    def get_token(self) -> str:
        headers = {"Referer": settings.http_client.client_url}
        response = self.get(ApiRoute.LOGIN, headers=headers)
        return response.cookies.get('csrftoken')


def get_authentication_client() -> AuthenticationClient:
    return AuthenticationClient(client=get_public_http_client())