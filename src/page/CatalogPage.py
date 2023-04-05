import time

from src.locators.CatalogLocator import Cataloglocator
from src.page.WelcomePage import WelcomePage


class CatalogPage(WelcomePage):
    def open_catalog_page(self):
        self.click_enter_button()

    def add_code_smell(self):
        self.click(locator=Cataloglocator.add_code_smell)
