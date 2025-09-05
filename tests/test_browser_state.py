import allure
import pytest
from allure_commons.types import Severity

from config import settings
from pages.home_page import HomePage
from utils.allure.stories import AllureStory
from utils.routes import AppRoute
from utils.allure.tags import AllureTag



@allure.severity(Severity.NORMAL)
@allure.story(AllureStory.VALID_LOGIN)
@allure.tag(AllureTag.USER_LOGIN)
@allure.title('User open home page with state logged in')
@pytest.mark.regression
@pytest.mark.flaky(reruns=3, reruns_delay=5,)
def test_open_logged_in(home_page_with_state: HomePage):
    home_page_with_state.visit(AppRoute.HOME)
    home_page_with_state.navbar.check_visible()
    home_page_with_state.navbar.check_to_be_logged(username=settings.test_user.username)