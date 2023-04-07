from src.locators.new_task_locators import NewTaskLocators
from src.page.list_task_page import ListTaskPage


class NewTaskPage(ListTaskPage):
    def open_page_new_task(self):
        self.click_new_task_list_task()

    def page_title_new_task(self) -> str:
        return self.return_text(locator=NewTaskLocators.TITLE_PAGE)

    def send_name_new_task(self, name: str) -> None:
        self.send_text(locator=NewTaskLocators.FIELD_NAME_TASK, text=name)

    def send_descriprion_new_task(self, descriprion: str) -> None:
        self.send_text(locator=NewTaskLocators.FIELD_DESCRIPRION_TASK, text=descriprion)

    def save_task_new_task(self) -> None:
        self.click(locator=NewTaskLocators.BUTTON_SAVE_TASK)

    def text_notification_warning(self) -> str:
        return self.return_text(locator=NewTaskLocators.NOTICE_WARNING)
