from playwright.sync_api import Locator
from elements.input import Input


class Textarea(Input):
    @property
    def type_of(self) ->str:
        return 'textarea'

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        return super().get_locator(nth, **kwargs).locator('textarea').first