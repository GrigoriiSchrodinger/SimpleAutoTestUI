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
        page.open_page_new_task()

        self.assertEqual(page.page_title_new_task(), "New Task")

    def test_create_new_task_case_02(self):
        """Проверяем что задача создается"""
        page = NewTaskPage(self.driver)
        page.open_page_new_task()
        page.send_name_new_task(name="hello")
        page.send_descriprion_new_task(descriprion="world")
        page.save_task_new_task()
        self.assertEqual(page.text_notification_list_task(), "Task added")

    def test_creation_without_description_case_03(self):
        """Проверяем что задача не может создавться без описания"""
        page = NewTaskPage(self.driver)
        page.open_page_new_task()
        page.send_name_new_task(name="hello")
        page.save_task_new_task()

        self.assertEqual(page.text_notification_warning(), "Tasks cannot be empty")

    def test_creation_without_name_case_04(self):
        """Проверяем что задача не может создавться без названия"""
        page = NewTaskPage(self.driver)
        page.open_page_new_task()
        page.send_descriprion_new_task(descriprion="world")
        page.save_task_new_task()

        self.assertEqual(page.text_notification_warning(), "Tasks cannot be empty")

    def tearDown(self) -> None:
        self.driver.quit()
