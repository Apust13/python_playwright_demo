import allure
from httpx import Response

from api_clients.api_client import APIClient
from api_clients.authentication.authentication_schema import AuthenticationUserSchema
from api_clients.private_http_builder import get_private_http_client
from utils.api_routes import ApiRoute


class PrivateUserClient(APIClient):

    @allure.step("Delete user {user}")
    def delete_user_api(self, user: AuthenticationUserSchema) ->Response:
        return self.delete(ApiRoute.DELETE_ACCOUNT, data=user.model_dump() )

    def delete_user(self, user: AuthenticationUserSchema):
        response = self.delete_user_api(user)
        return response.json()

def get_private_user_client(user: AuthenticationUserSchema) -> PrivateUserClient:
    return PrivateUserClient(client=get_private_http_client(user))