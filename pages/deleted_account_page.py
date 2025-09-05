from playwright.sync_api import Page, expect

from elements.text import Text
from pages.account_created_page import AccountCreatedPage


class DeletedAccountPage(AccountCreatedPage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.account_deleted_title = Text(page, '[data-qa="account-deleted"]', 'Account deleted')


    def check_visible(self):
        self.account_deleted_title.check_visible()
        self.account_deleted_title.check_have_text('ACCOUNT DELETED!', ignore_case=True)
        self.check_visible_continue_button()