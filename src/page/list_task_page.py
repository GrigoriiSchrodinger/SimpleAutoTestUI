from src.locators.list_task_locators import ListTaskLocators
from src.page.BasePage import BasePage


class ListTaskPage(BasePage):
    """
    Страница со списками задачами.

    Нейминг, на который стоит обратить внимание:
    def имя_страницы_действие_кнопка(self):
        ....
    """
    def list_task_click_new_task(self) -> None:
        self.click(locator=ListTaskLocators.BUTTON_ADD_TASK)

    def list_task_return_text_notice_add_task(self) -> str:
        return self.return_text(locator=ListTaskLocators.NOTICE_ADD_TASK)




