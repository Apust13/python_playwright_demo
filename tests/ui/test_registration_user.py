import pytest
import allure
from allure_commons.types import Severity

from utils.allure.tags import AllureTag
from utils.allure.epics import AllureEpic
from utils.allure.features import AllureFeature
from utils.allure.stories import AllureStory
from pages.account_created_page import AccountCreatedPage
from pages.deleted_account_page import DeletedAccountPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from utils.ui_routes import AppRoute


@allure.epic(AllureEpic.SIGNUP)
@allure.feature(AllureFeature.REGISTRATION)
@allure.tag(AllureTag.AUTHORIZATION)
@pytest.mark.regression
@pytest.mark.smoke
class TestAuthorization:

    @allure.severity(Severity.CRITICAL)
    @allure.story(AllureStory.SIGNUP)
    @allure.tag(AllureTag.REGISTRATION)
    @allure.title('New User Registration')
    def test_registration_user(
            self,
            home_page: HomePage,
            login_page: LoginPage,
            signup_page: SignupPage,
            account_created_page: AccountCreatedPage,
            deleted_account_page: DeletedAccountPage
    ):
        home_page.visit(AppRoute.HOME)
        home_page.navbar.go_to_login_page()

        login_page.fill_signup_form('test1', 'tes32ds2111@em23ail.com')
        login_page.click_signup_button()

        signup_page.check_signup_form_visible(name='test1', email='tes32ds2111@em23ail.com')
        signup_page.fill_signup_form(
            title='Mr',
            password='12345678',
            day_of_birth='3',
            month_of_birth='June',
            year_of_birth='1980',

            first_name='Jim',
            last_name='Root',
            company='Slipknot',
            address='Palm st, 12',
            country='United States',
            state='IOWA',
            city='Des Moines',
            zipcode='1233111',
            mobile_number='3454574523'
        )

        signup_page.click_create_account_button()

        account_created_page.check_visible()
        account_created_page.click_continue_button()

        home_page.navbar.check_visible()
        home_page.navbar.check_to_be_logged(username='test1')
        home_page.navbar.click_delete_account_button()

        deleted_account_page.check_visible()
        deleted_account_page.click_continue_button()


    @allure.severity(Severity.BLOCKER)
    @allure.story(AllureStory.VALID_LOGIN)
    @allure.tag(AllureTag.USER_LOGIN)
    @allure.title('User login with valid email and password')
    @pytest.mark.parametrize(
        'email, password, username',
        [
            ('jimds2111@em23ail.com', '12345678', 'Jim'),
            ('fred23@email.com', '12345678', 'Fred')
        ]
    )
    def test_login_user_with_correct_email_and_password(
            self,
            home_page: HomePage,
            login_page: LoginPage,
            signup_page: SignupPage,
            account_created_page: AccountCreatedPage,
            deleted_account_page: DeletedAccountPage,
            email: str,
            password: str,
            username: str
    ):
        home_page.visit(AppRoute.HOME)
        home_page.navbar.go_to_login_page()
        login_page.fill_login_form(email=email, password=password)
        login_page.click_login_button()

        home_page.navbar.check_visible()
        home_page.navbar.check_to_be_logged(username=username)
