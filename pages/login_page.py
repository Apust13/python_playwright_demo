import re

from components.navigation.navbar_component import NavbarComponent
from elements.button import Button
from elements.input import Input
from elements.text import Text
from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)

        self.signup_form_title = Text(page, '.signup-form>h2', 'New User Signup')
        self.signup_form_name_input = Input(page, '[data-qa="signup-name"]', 'Name')
        self.signup_form_email_input = Input(page,'[data-qa="signup-email"]', 'Email Address')
        self.sign_up_button = Button(page, '[data-qa="signup-button"]', 'Signup')

        self.login_form_title = Text(page, '.login-form>h2', 'Login to your account')
        self.login_form_email_input = Input(page, '[data-qa="login-email"]', 'Email Address')
        self.login_form_password_input = Input(page, '[data-qa="login-password"]', 'Password')
        self.login_button = Button(page, '[data-qa="login-button"]', 'Login')


    def fill_signup_form(self, name: str, email: str):
        self.signup_form_name_input.fill(name)
        self.signup_form_name_input.check_have_value(name)

        self.signup_form_email_input.fill(email)
        self.signup_form_email_input.check_have_value(email)


    def click_signup_button(self):
        self.sign_up_button.click()

    def fill_login_form(self, email: str,  password: str):
        self.login_form_email_input.fill(email)
        self.login_form_email_input.check_have_value(email)

        self.login_form_password_input.fill(password)
        self.login_form_password_input.check_have_value(password)


    def click_login_button(self):
        self.login_button.click()
