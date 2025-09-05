from playwright.sync_api import Page, expect

from elements.button import Button
from elements.text import Text
from pages.base_page import BasePage


class AccountCreatedPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.account_created_title = Text(page, '[data-qa="account-created"]', 'Account created')
        self.continue_button = Button(page,'[data-qa="continue-button"]', 'Continue')

    def check_visible_continue_button(self):
        self.continue_button.check_visible()
        self.continue_button.check_have_text('Continue')

    def check_visible(self):
        self.account_created_title.check_visible()
        self.account_created_title.check_have_text('ACCOUNT CREATED!', ignore_case=True)
        self.check_visible_continue_button()




    def click_continue_button(self):
        self.check_visible_continue_button()
        self.continue_button.click()