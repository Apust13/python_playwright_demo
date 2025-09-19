import allure
from httpx import Response

from api_clients.api_client import APIClient
from api_clients.authentication.authentication_schema import AuthenticationUserSchema
from api_clients.public_http_builder import get_public_http_client
from api_clients.users.users_schema import CreateUserRequestSchema, UserDetailSchema, UserEmailSchema
from utils.api_routes import ApiRoute


class PublicUserClient(APIClient):


    @allure.step("Create user with details {user_info}")
    def create_user_api(self, user_info: CreateUserRequestSchema) -> Response:
        return self.post(ApiRoute.CREATE_ACCOUNT, data=user_info.model_dump())


    @allure.step("Create user")
    def create_user(self, request: CreateUserRequestSchema):
        request = self.create_user_api(request)
        return request.json()

    @allure.step("Check that user has been created {request}")
    def check_user_existence_api(self, request: AuthenticationUserSchema) -> Response:
        return self.post(ApiRoute.VERIFY_LOGIN, data=request.model_dump())

    @allure.step("Check that user has been created")
    def check_user_existence(self, request: AuthenticationUserSchema):
        response = self.check_user_existence_api(request=request)
        return response.json()

    @allure.step("Get user info by {request}")
    def get_user_api(self, request: UserEmailSchema) -> Response:
        return self.get(ApiRoute.GET_USER_DETAIL_BY_EMAIL, params=request.model_dump())

    @allure.step("Get user info")
    def get_user(self, request: UserEmailSchema) -> UserDetailSchema:
        response = self.get_user_api(request)
        return UserDetailSchema.model_validate(response.json()['user'])


def get_public_user_client() -> PublicUserClient:
    return PublicUserClient(client=get_public_http_client())