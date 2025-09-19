from http import HTTPStatus

import allure
import pytest

from api_clients.authentication.authentication_schema import AuthenticationUserSchema
from api_clients.users.public_user_client import PublicUserClient
from api_clients.users.users_schema import UserResponseSchema, UserEmailSchema
from utils.allure.epics import AllureEpic
from utils.allure.features import AllureFeature
from utils.allure.tags import AllureTag
from utils.api.assertions.base import assert_status_code
from utils.api.assertions.users import assert_user_exist_response


@allure.epic(AllureEpic.SIGNUP)
@allure.feature(AllureFeature.REGISTRATION)
@pytest.mark.regression
@pytest.mark.api
class TestCheckUser:


    @pytest.mark.flaky(reruns=2, reruns_delay=2)
    @allure.title('Check that user exist')
    @allure.tag(AllureTag.REGISTRATION, AllureTag.VALIDATE_ENTITY)
    def test_user_exists(self, user_credentials: dict[str, str], public_client: PublicUserClient):
        check_user_request = AuthenticationUserSchema(
            email=user_credentials['email'],
            password=user_credentials['password']
        )
        user_exist_response = public_client.check_user_existence_api(request=check_user_request)
        user_exist_response_data = UserResponseSchema.model_validate_json(user_exist_response.text)

        print(user_exist_response)
        print(user_exist_response.json())

        assert_status_code(user_exist_response.status_code, HTTPStatus.OK)
        assert_user_exist_response(user_exist_response_data)


    @allure.title('Check user details')
    @allure.tag(AllureTag.REGISTRATION, AllureTag.VALIDATE_ENTITY)
    def test_check_user_details(self, user_credentials: dict[str, str], public_client: PublicUserClient):
        check_user_request = UserEmailSchema(
            email =user_credentials['email'],
        )
        check_user_response = public_client.get_user_api(request=check_user_request)
        print(check_user_response.json())
        assert_status_code(check_user_response.status_code, HTTPStatus.OK)