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

    def list_task_click_drop_down_box(self) -> None:
        self.click(locator=ListTaskLocators.BUTTON_DROP_DOWN_BOX)

    def list_task_click_refresh(self) -> None:
        self.click(locator=ListTaskLocators.BUTTON_DROP_DOWN_BOX_REFRESH)

    def list_task_click_task(self, number_task: int) -> None:
        self.click(locator=(
            ListTaskLocators.TASK[0],
            ListTaskLocators.TASK[1].format(number_task=number_task)
        ))

    def list_task_return_name_task(self, number_task: int) -> str:
        return self.return_text(locator=(
            ListTaskLocators.TASK_NAME[0],
            ListTaskLocators.TASK_NAME[1].format(number_task=number_task),
        ))





