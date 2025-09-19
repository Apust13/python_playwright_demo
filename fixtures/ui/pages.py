import pytest
from playwright.sync_api import Page

from fixtures.ui.browsers import page_with_state
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from pages.account_created_page import AccountCreatedPage
from pages.deleted_account_page import DeletedAccountPage

@pytest.fixture
def home_page(page: Page) -> HomePage:
    return HomePage(page=page)

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page=page)

@pytest.fixture
def signup_page(page: Page) -> SignupPage:
    return SignupPage(page=page)

@pytest.fixture
def account_created_page(page: Page) -> AccountCreatedPage:
    return AccountCreatedPage(page=page)

@pytest.fixture
def deleted_account_page(page: Page) -> DeletedAccountPage:
    return DeletedAccountPage(page=page)

@pytest.fixture
def home_page_with_state(page_with_state: Page) -> HomePage:
    return HomePage(page=page_with_state)
