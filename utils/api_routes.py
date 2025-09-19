from enum import Enum


class ApiRoute(str, Enum):
    LOGIN = '/login'
    PRODUCTS_LIST = '/api/productsList'
    SEARCH_PRODUCT = '/api/searchProduct'
    DELETE_ACCOUNT = '/api/deleteAccount'
    CREATE_ACCOUNT = '/api/createAccount'
    VERIFY_LOGIN = '/api/verifyLogin'
    GET_USER_DETAIL_BY_EMAIL = '/api/getUserDetailByEmail'
