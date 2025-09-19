from http import HTTPStatus

import allure
import pytest
from allure_commons.types import Severity

from api_clients.authentication.authentication_client import AuthenticationClient
from api_clients.users.users_schema import LoginRequestSchema
from config import settings
from utils.allure.epics import AllureEpic
from utils.allure.features import AllureFeature
from utils.allure.stories import AllureStory
from utils.allure.tags import AllureTag
from utils.api.assertions.base import assert_status_code_contains


@allure.epic(AllureEpic.SIGNUP)
@allure.feature(AllureFeature.REGISTRATION)
@allure.title('Login by valid credentials')
@pytest.mark.api
@pytest.mark.regression
class TestAuthentication:

    @allure.severity(Severity.CRITICAL)
    @allure.story(AllureStory.SIGNUP)
    @allure.tag(AllureTag.USER_LOGIN)
    def test_login(self, authentication_client: AuthenticationClient):
        login_request = LoginRequestSchema(email=settings.test_user.email,password=settings.test_user.password)
        login_response = authentication_client.login_api(login_request)
        assert_status_code_contains(login_response.status_code, HTTPStatus.FOUND , HTTPStatus.OK)
