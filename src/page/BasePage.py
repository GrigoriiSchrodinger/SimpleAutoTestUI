from src.utils.config import IMPLICIT_WAIT


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator: tuple) -> None:
        self.driver.implicitly_wait(IMPLICIT_WAIT)
        self.driver.find_element(*locator).click()

    def return_text(self, locator: tuple) -> str:
        self.driver.implicitly_wait(IMPLICIT_WAIT)
        return self.driver.find_element(*locator).text
