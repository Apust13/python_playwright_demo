import allure
from playwright.sync_api import expect

from elements.base_element import BaseElement
from utils.logger import get_logger

logger = get_logger("CHECKBOX")


class CheckBox(BaseElement):
    @property
    def type_of(self) ->str:
        return 'checkbox'


    def check(self, nth: int = 0, **kwargs):
        step = f'Check {self.type_of} "{self.name}"'
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            locator.check()


    def check_is_checked(self, nth: int = 0, **kwargs):
        step = f'Checking that {self.type_of} "{self.name}" is checked'
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_be_checked()


    def check_is_not_checked(self, nth: int = 0, **kwargs):
        step = f'Checking that {self.type_of} "{self.name}" is not checked'
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).not_to_be_checked()