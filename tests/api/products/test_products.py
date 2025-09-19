from http import HTTPStatus

import pytest

from api_clients.authentication.authentication_client import AuthenticationClient
from api_clients.authentication.authentication_schema import AuthenticationUserSchema
from api_clients.products.products_client import get_private_products_client
from api_clients.users.users_schema import LoginRequestSchema
from config import settings
from utils.api.assertions.base import assert_status_code_contains


@pytest.mark.regression
@pytest.mark.products
class TestProducts:

    # @pytest.mark.skip
    def test_add_products_to_cart(self, authentication_client: AuthenticationClient):
        login_request = LoginRequestSchema(email=settings.test_user.email, password=settings.test_user.password)
        login_response = authentication_client.login_api(login_request)
        assert_status_code_contains(login_response.status_code, HTTPStatus.FOUND, HTTPStatus.OK)

        auth = AuthenticationUserSchema(email=login_request.email, password=login_request.password)
        products_client = get_private_products_client(auth)
        products = products_client.get_all_products()
       

