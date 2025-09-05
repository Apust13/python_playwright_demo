import allure
from elements.base_element import BaseElement
from utils.logger import get_logger

logger = get_logger("SELECT")

class Select(BaseElement):
    @property
    def type_of(self) -> str:
        return 'select'

    def select(self, value:str, nth: int = 0, **kwargs):
        step = f'Fill {self.type_of} "{self.name}" to value "{value}"'
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            locator.select_option(value)