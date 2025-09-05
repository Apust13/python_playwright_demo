from enum import Enum

class AllureStory(str, Enum):
    SIGNUP = 'Signup of new user'
    VALID_LOGIN = 'Login by valid credentials'
    INVALID_LOGIN = 'Login by wrong credentials'