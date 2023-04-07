from src.locators.new_task_locators import NewTaskLocators
from src.page.list_task_page import ListTaskPage


class NewTaskPage(ListTaskPage):
    """
    Страница создание задачи.

    Нейминг, на который стоит обратить внимание:
    def имя_страницы_действие_кнопка(self):
        ....
    """
    def new_task_open_page(self) -> None:
        self.list_task_click_new_task()

    def new_task_return_text_title_page(self) -> str:
        return self.return_text(locator=NewTaskLocators.TITLE_PAGE)

    def new_task_send_name_task(self, name: str) -> None:
        self.send_text(locator=NewTaskLocators.FIELD_NAME_TASK, text=name)

    def new_task_send_description_task(self, description: str) -> None:
        self.send_text(locator=NewTaskLocators.FIELD_DESCRIPTION_TASK, text=description)

    def new_task_click_save_task(self) -> None:
        self.click(locator=NewTaskLocators.BUTTON_SAVE_TASK)

    def new_task_return_text_notice_warning(self) -> str:
        return self.return_text(locator=NewTaskLocators.NOTICE_WARNING)
