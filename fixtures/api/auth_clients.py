import pytest

from api_clients.authentication.authentication_client import AuthenticationClient, get_authentication_client
from api_clients.authentication.authentication_schema import AuthenticationUserSchema
from api_clients.users.private_user_client import PrivateUserClient, get_private_user_client
from api_clients.users.public_user_client import PublicUserClient, get_public_user_client


@pytest.fixture
def authentication_client() -> AuthenticationClient:
    return get_authentication_client()


@pytest.fixture
def public_client() -> PublicUserClient:
    return get_public_user_client()


@pytest.fixture
def private_client(user: AuthenticationUserSchema) -> PrivateUserClient:
    return get_private_user_client(user=user)


