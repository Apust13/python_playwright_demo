from playwright.sync_api import Locator

from elements.base_element import BaseElement


class RadioButton(BaseElement):
    @property
    def type_of(self) -> str:
        return 'radio_button'