class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator: tuple) -> None:
        self.driver.implicitly_wait(30)
        self.driver.find_element(*locator).click()

    def return_text(self, locator: tuple) -> str:
        self.driver.implicitly_wait(30)
        return self.driver.find_element(*locator).text
