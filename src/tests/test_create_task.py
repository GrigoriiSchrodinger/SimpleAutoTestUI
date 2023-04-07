import logging
import unittest

from appium import webdriver

from src.page.new_task_page import NewTaskPage
from src.utils.config import DESIRED_CAPABILITIES, APPIUM_URL

logger = logging.getLogger("root")


class TestsCreateTask(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(
            command_executor=APPIUM_URL,
            desired_capabilities=DESIRED_CAPABILITIES
        )

    def test_open_new_task_case_01(self) -> None:
        """Проверяем что страница создания открывается"""
        page = NewTaskPage(self.driver)
        page.new_task_open_page()

        self.assertEqual(page.new_task_return_text_title_page(), "New Task")

    def test_create_new_task_case_02(self):
        """Проверяем что задача создается"""
        page = NewTaskPage(self.driver)
        page.new_task_open_page()

        page.new_task_send_name_task(name="hello")
        page.new_task_send_description_task(descriprion="world")
        page.new_task_click_save_task()

        self.assertEqual(page.list_task_return_text_notice_add_task(), "Task added")

    def test_creation_without_description_case_03(self):
        """Проверяем что задача не может создавться без описания"""
        page = NewTaskPage(self.driver)
        page.new_task_open_page()

        page.new_task_send_name_task(name="hello")
        page.new_task_click_save_task()

        self.assertEqual(page.new_task_return_text_notice_warning(), "Tasks cannot be empty")

    def test_creation_without_name_case_04(self):
        """Проверяем что задача не может создавться без названия"""
        page = NewTaskPage(self.driver)
        page.new_task_open_page()

        page.new_task_send_description_task(descriprion="world")
        page.new_task_click_save_task()

        self.assertEqual(page.new_task_return_text_notice_warning(), "Tasks cannot be empty")

    def tearDown(self) -> None:
        self.driver.quit()
