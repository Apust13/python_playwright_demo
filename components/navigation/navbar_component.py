import re

import allure

from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

from components.navigation.navbar_list_item import NavbarListItem
from elements.link import Link
from elements.text import Text


class NavbarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.home_item = NavbarListItem(page,'/')
        self.products_item = NavbarListItem(page,'/products')
        self.cart_item = NavbarListItem(page,'/view_cart')
        self.signup_login_item = NavbarListItem(page,'/login')
        self.logout_item = NavbarListItem(page,'/logout')
        self.delete_account_item = NavbarListItem(page, '/delete_account')
        self.test_cases_item = NavbarListItem(page,'/test_cases')
        self.api_testing_item = NavbarListItem(page,'/api_list')
        self.contact_us_item = NavbarListItem(page,'/contact_us')

        self.video_tutorials_item = Link(page, '.navbar-nav a[href$="/AutomationExercise', 'Video tutorials')
        self.logged_title = Text(page,'.navbar-nav :last-child a', 'Logged title')

    @allure.step('Checking that navbar is visible')
    def check_visible(self):
        self.home_item.check_visible("Home")
        self.products_item.check_visible("Products")
        self.cart_item.check_visible("Cart")


    def go_to_login_page(self):
        self.signup_login_item.navigate(re.compile(r".*/login"))
        self.check_current_url(re.compile('.*/login'))

    @allure.step('Checking that user {username} is logged in')
    def check_to_be_logged(self, username: str):
        self.logout_item.check_visible('Logout')
        self.delete_account_item.check_visible('Delete Account')

        self.logged_title.check_visible()
        self.logged_title.check_have_text(f'Logged in as {username}')

    @allure.step('Clicking "Delete Account"')
    def click_delete_account_button(self):
        self.delete_account_item.navigate(re.compile(r".*/delete_account"))