from http import HTTPStatus

import allure
import pytest

from api_clients.users.public_user_client import PublicUserClient
from api_clients.users.users_schema import UserResponseSchema
from utils.allure.tags import AllureTag
from utils.api.assertions.base import assert_status_code
from utils.api.assertions.users import assert_delete_user_response, assert_user_not_found_response


@pytest.mark.api
class TestDeleteUsers:

    @allure.tag(AllureTag.DELETE_ENTITIES)
    @pytest.mark.skip
    def test_delete_users(self, function_get_user, public_client: PublicUserClient):
        client, schema = function_get_user

        print(schema)

        delete_user_response = client.delete_user_api(schema)
        delete_user_response_data = UserResponseSchema.model_validate_json(delete_user_response.text)

        print(delete_user_response.status_code, delete_user_response.json())

        assert_status_code(delete_user_response.status_code, HTTPStatus.OK)
        assert_delete_user_response(delete_user_response_data)

        user_not_found_response = public_client.check_user_existence_api(request=schema)
        user_not_found_response_data = UserResponseSchema.model_validate_json(user_not_found_response.text)

        print(user_not_found_response)
        print(user_not_found_response.json())

        assert_status_code(user_not_found_response.status_code, HTTPStatus.OK)
        assert_user_not_found_response(user_not_found_response_data)