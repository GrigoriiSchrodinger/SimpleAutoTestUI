from src.locators.NewTaskLocators import NewTaskLocators
from src.page.ListTaskPage import ListTaskPage


class NewTaskPage(ListTaskPage):
    def open_page_new_task(self):
        self.click_new_task()

    def page_title_new_task(self) -> str:
        return self.return_text(NewTaskLocators.TITLE_PAGE)
