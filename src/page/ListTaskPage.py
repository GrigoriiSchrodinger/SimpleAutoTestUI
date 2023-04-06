from src.locators.ListTaskLocators import ListTaskLocators
from src.page.BasePage import BasePage


class ListTaskPage(BasePage):
    def click_new_task(self) -> None:
        self.click(locator=ListTaskLocators.BUTTON_ADD_TASK)




