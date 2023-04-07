from src.locators.list_task_locators import ListTaskLocators
from src.page.BasePage import BasePage


class ListTaskPage(BasePage):
    def click_new_task_list_task(self) -> None:
        self.click(locator=ListTaskLocators.BUTTON_ADD_TASK)

    def text_notification_list_task(self) -> str:
        return self.return_text(ListTaskLocators.NOTICE_ADD_TASK)




