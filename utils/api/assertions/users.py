from http import HTTPStatus

import allure

from api_clients.users.users_schema import CreateUserRequestSchema, GetUserResponseSchema, \
    UserResponseSchema
from utils.api.assertions.base import assert_equal
from utils.logger import get_logger

logger = get_logger("USERS_ASSERTIONS")

@allure.step("Check user details response")
def assert_check_user_details_response(request: CreateUserRequestSchema, response: GetUserResponseSchema):
    logger.info('Check user details response')

    assert_equal(response.user.email, request.email, 'email')
    assert_equal(response.user.name, request.name, 'name')
    assert_equal(response.user.firstname, request.firstname, 'first name')
    assert_equal(response.user.lastname, request.lastname, 'last name')
    assert_equal(response.user.company, request.company, 'company')
    assert_equal(response.user.address1, request.address1, 'address 1')
    assert_equal(response.user.address2, request.address2, 'address 2')
    assert_equal(response.user.country, request.country, 'country')
    assert_equal(response.user.state, request.state, 'state')
    assert_equal(response.user.city, request.city, 'city')
    assert_equal(response.user.zipcode, request.zipcode, 'zipcode')


def assert_user_response(response: UserResponseSchema, text_message: str, status_code: HTTPStatus):
    assert_equal(response.message, text_message,'message')
    assert_equal(response.response_code, status_code,'message')


@allure.step("Check create user response")
def assert_create_user_response(response: UserResponseSchema):
    logger.info('Check create user response')
    assert_user_response(response,'User created!', HTTPStatus.CREATED)


@allure.step("Check delete user response")
def assert_delete_user_response(response: UserResponseSchema):
    logger.info('Check create user response')
    assert_user_response(response, 'Account deleted!', HTTPStatus.OK)


@allure.step("Check user not found response")
def assert_user_not_found_response(response: UserResponseSchema):
    logger.info('Check user not found response')
    assert_user_response(response, 'User not found!', HTTPStatus.NOT_FOUND)


@allure.step("Check user exist response")
def assert_user_exist_response(response: UserResponseSchema):
    logger.info('Check user exist response')
    assert_user_response(response, 'User exists!', HTTPStatus.OK)
