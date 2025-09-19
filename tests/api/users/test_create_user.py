from http import HTTPStatus

import allure
import pytest
from allure_commons.types import Severity

from api_clients.users.public_user_client import PublicUserClient
from api_clients.users.users_schema import CreateUserRequestSchema, UserResponseSchema, UserEmailSchema, GetUserResponseSchema
from utils.allure.epics import AllureEpic
from utils.allure.features import AllureFeature
from utils.allure.stories import AllureStory
from utils.allure.tags import AllureTag
from utils.api.assertions.base import assert_status_code, assert_equal
from utils.api.assertions.schema import validate_json_schema
from utils.api.assertions.users import assert_create_user_response, assert_check_user_details_response
from utils.api.fakers import fake_builder
from utils.io_helper import save_credentials, get_credential


@allure.epic(AllureEpic.SIGNUP)
@allure.feature(AllureFeature.REGISTRATION)
@allure.tag(AllureTag.AUTHORIZATION)
@pytest.mark.regression
@pytest.mark.users
@pytest.mark.api
class TestCreateUser:

    @allure.severity(Severity.CRITICAL)
    @allure.story(AllureStory.SIGNUP)
    @allure.title('Create user')
    @allure.tag(AllureTag.REGISTRATION, AllureTag.CREATE_ENTITY, AllureTag.VALIDATE_ENTITY)
    def test_create_user(self, public_client: PublicUserClient):
        profile = fake_builder.person_profile()
        create_user_request = CreateUserRequestSchema(**profile)

        email = create_user_request.email
        password = create_user_request.password

        create_user_response = public_client.create_user_api(create_user_request)
        create_user_response_data = UserResponseSchema.model_validate_json(create_user_response.text)
        assert_create_user_response(create_user_response_data)

        validate_json_schema(create_user_response.json(), schema=create_user_response_data.model_json_schema())

        save_credentials(email, password)

        creds = get_credential()
        check_user_request = UserEmailSchema(
            email=creds['email']
        )
        check_user_response = public_client.get_user_api(request=check_user_request)
        check_user_response_data = GetUserResponseSchema.model_validate_json(check_user_response.text)

        assert_status_code(create_user_response.status_code, HTTPStatus.OK)
        assert_equal(create_user_response.json()['responseCode'], HTTPStatus.CREATED, 'response code')
        assert_check_user_details_response(create_user_request, check_user_response_data)