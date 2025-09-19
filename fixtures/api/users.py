import pytest
from _pytest.fixtures import SubRequest
from pydantic import BaseModel, EmailStr

from api_clients.authentication.authentication_schema import AuthenticationUserSchema
from api_clients.users.private_user_client import PrivateUserClient, get_private_user_client
from api_clients.users.public_user_client import PublicUserClient
from api_clients.users.users_schema import CreateUserRequestSchema, UserResponseSchema, LoginRequestSchema
from utils.api.fakers import fake_builder
from utils.io_helper import get_credential, save_credentials, get_creds, remove_credentials


class UserFixture(BaseModel):
    request: CreateUserRequestSchema
    response: UserResponseSchema

    @property
    def email(self) -> EmailStr:
        return self.request.email

    @property
    def password(self) -> str:
        return self.request.password

    @property
    def auth(self) -> AuthenticationUserSchema:
        return AuthenticationUserSchema(email=self.email, password=self.password)

    @property
    def login_request(self) -> LoginRequestSchema:
        return LoginRequestSchema(email=self.email, password=self.password)




@pytest.fixture
def user_credentials() -> dict[str, str]:
    creds = get_credential()
    yield creds


@pytest.fixture
def function_new_user(public_client: PublicUserClient) -> UserFixture:
    profile = fake_builder.person_profile()
    request = CreateUserRequestSchema(**profile)
    response = public_client.create_user(request)

    save_credentials(email=request.email, password=request.password)
    return  UserFixture(request=request, response=response)


@pytest.fixture(params=get_creds())
def function_get_user(request: SubRequest) -> tuple[PrivateUserClient, AuthenticationUserSchema]:
    email = request.param['email']
    password = request.param['password']
    schema = AuthenticationUserSchema(email=email, password=password)
    client = get_private_user_client(schema)

    yield client, schema

    remove_credentials(email, password)


