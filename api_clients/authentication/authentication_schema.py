from pydantic import BaseModel, Field, EmailStr, ConfigDict

from utils.api.fakers import fake


class AuthenticationUserSchema(BaseModel):
    model_config = ConfigDict(frozen=True)

    email: EmailStr = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)

