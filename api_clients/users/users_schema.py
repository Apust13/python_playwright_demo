from typing import Annotated

from pydantic import BaseModel, EmailStr, Field, ConfigDict

from utils.api.fakers import fake

class UserEmailSchema(BaseModel):
    email: EmailStr = Field(default_factory=fake.email)

class UserInfoSchema(UserEmailSchema):
    model_config = ConfigDict(populate_by_name=True)

    name: str = Field(default_factory=fake.name)
    title: str = Field(default_factory=fake.title)
    birth_day: str = Field(default_factory=fake.birth_day)
    birth_month: str = Field(default_factory=fake.birth_month)
    birth_year: str = Field(default_factory=fake.birth_year)
    firstname: str = Field(alias="first_name", default_factory=fake.first_name)
    lastname: str = Field(alias="last_name", default_factory=fake.last_name)
    company: str = Field(default_factory=fake.company)
    address1: str = Field(default_factory=fake.address_1)
    address2: str = Field(default_factory=fake.address_2)
    country: str = Field(default_factory=fake.country)
    state: str = Field(default_factory=fake.state)
    city: str = Field(default_factory=fake.city)
    zipcode: str = Field(default_factory=fake.zipcode)


class CreateUserRequestSchema(UserInfoSchema):
    password: str  = Field(default_factory=fake.password)
    mobile_number: str  = Field(default_factory=fake.mobile_number)


class UserDetailSchema(UserInfoSchema):
    id: int = Field(default_factory=fake.uuid)

class GetUserResponseSchema(BaseModel):
    user: UserDetailSchema


class UserResponseSchema(BaseModel):
    message: str
    response_code: int = Field(alias="responseCode")


class LoginRequestSchema(UserEmailSchema):
    password: str = Field(default_factory=fake.password)
    token: Annotated[str | None, Field(alias="csrfmiddlewaretoken")] = None
