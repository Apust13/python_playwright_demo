import allure
from playwright.sync_api import Page, Locator, expect

from utils.logger import get_logger

logger = get_logger("BASE_ELEMENT")

class BaseElement:
    def __init__(self, page: Page, locator: str, name: str):
        self.page = page
        self.locator = locator
        self.name = name


    @property
    def type_of(self)->str:
        return 'base element'


    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        locator = self.locator.format(**kwargs)
        step = f'Getting locator={locator} at index "{nth}"'
        with allure.step(step):
            logger.info(step)
            return self.page.locator(locator).nth(nth)


    def click(self, nth: int = 0, **kwargs):
        step = f'Clicking {self.type_of} "{self.name}"'
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            locator.click()


    def check_visible(self, nth: int = 0, **kwargs):
        step = f'Checking that {self.type_of} "{self.name}" is visible'
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_be_visible()


    def check_have_text(self, text:str, nth: int = 0, strict: bool = True, ignore_case: bool = False, **kwargs):
        mode = 'has' if strict else 'contains'
        step = f'Checking that {self.type_of} "{self.name}" {mode} text "{text}"'
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            if strict:
                expect(locator).to_have_text(text, ignore_case=ignore_case)
            else:
                expect(locator).to_contain_text(text, ignore_case=ignore_case)

