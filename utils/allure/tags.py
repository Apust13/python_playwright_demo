from enum import Enum

class AllureTag(str, Enum):
    USER_LOGIN = 'USER_LOGIN'
    REGISTRATION = 'REGISTRATION'
    AUTHORIZATION = 'AUTHORIZATION'
