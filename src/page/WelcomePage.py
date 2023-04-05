from src.locators.WelcomeLocators import WelcomeLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator: tuple) -> None:
        self.driver.implicitly_wait(30)
        self.driver.find_element(*locator).click()


class WelcomePage(BasePage):
    def click_enter_button(self):
        self.click(locator=WelcomeLocators.ENTER_BUTTON)


