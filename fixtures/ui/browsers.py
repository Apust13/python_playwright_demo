import pytest
from _pytest.fixtures import SubRequest
from playwright.sync_api import Playwright, Page

from config import settings
from pages.login_page import LoginPage
from utils.playwright.mocks import mock_static_resources
from utils.playwright.pages import initialize_playwright_page
from utils.ui_routes import AppRoute


@pytest.fixture(params=settings.browsers)
def page(request: SubRequest, playwright: Playwright) -> Page:
    yield from initialize_playwright_page(
        playwright,
        test_name=request.node.name,
        browser_type=request.param
    )


@pytest.fixture(scope='session', params=settings.browsers)
def initialize_browser_state(request: SubRequest, playwright: Playwright):
        browser_type = request.param
        browser = playwright[browser_type].launch(headless=settings.headless)
        context = browser.new_context(base_url=settings.get_base_url())
        page = context.new_page()
        # mock_static_resources(page)

        login_page = LoginPage(page=page)
        login_page.visit(AppRoute.LOGIN, wait_until='networkidle')
        login_page.fill_login_form(email=settings.test_user.email, password=settings.test_user.password)
        login_page.click_login_button()

        context.storage_state(path=settings.browser_state_file)
        browser.close()


@pytest.fixture(params=settings.browsers)
def page_with_state(request: SubRequest, initialize_browser_state, playwright: Playwright) -> Page:
    yield from initialize_playwright_page(
        playwright,
        test_name=request.node.name,
        browser_type=request.param,
        storage_state= settings.browser_state_file
    )
