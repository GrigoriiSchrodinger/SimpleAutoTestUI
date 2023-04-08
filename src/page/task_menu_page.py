from src.locators.task_menu_locators import TaskMenuLocators
from src.page.list_task_page import ListTaskPage


class MenuTask(ListTaskPage):
    """
    Страница создание задачи.

    Нейминг, на который стоит обратить внимание:
    def имя_страницы_действие_кнопка(self):
        ....
    """
    def menu_task_click_delete(self):
        self.click(locator=TaskMenuLocators.BUTTON_DELETE)


