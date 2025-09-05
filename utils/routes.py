from enum import Enum

class AppRoute(str, Enum):
    LOGIN = '/login'
    HOME = '/'
    PRODUCTS = '/products'
    CART = '/view_cart'
    LOGOUT = '/logout'
    DELETE_ACCOUNT = '/delete_account'
    TEST_CASES = '/test_cases'
    API = '/api_list'
    CONTACT_US = '/contact_us'
