from re import Pattern

import allure
from playwright.sync_api import Page


from components.base_component import BaseComponent
from elements.icon import Icon
from elements.link import Link


class NavbarListItem(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.icon = Icon(page, f'.navbar-nav a[href="{identifier}"]>i', 'Navbar icon')
        self.link = Link(page, f'.navbar-nav a[href="{identifier}"]', 'Navbar link')

    @allure.step('Check visible {title} navbar item')
    def check_visible(self, title: str):
        self.icon.check_visible()
        self.link.check_visible()
        self.link.check_have_text(title, strict=False)

    def navigate(self, expected_url: Pattern[str]):
        self.link.click()
        self.check_current_url(expected_url)