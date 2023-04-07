import logging

from appium.webdriver import WebElement

from src.utils.config import IMPLICIT_WAIT

logger = logging.getLogger('root')


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator) -> WebElement:
        logger.debug(f"find - {locator}")
        self.driver.implicitly_wait(IMPLICIT_WAIT)
        return self.driver.find_element(*locator)

    def click(self, locator: tuple) -> None:
        logger.debug(f"Click - {locator}")
        self.find_element(locator=locator).click()

    def return_text(self, locator: tuple) -> str:
        logger.debug(f"Return text - {locator}")
        return self.find_element(locator=locator).text

    def send_text(self, locator: tuple, text: str) -> None:
        logger.debug(f"Send text - {locator}")
        self.find_element(locator=locator).send_keys(text)



