import unittest

from appium import webdriver
from src.page.NewTaskPage import NewTaskPage
from src.utils.config import DESIRED_CAPABILITIES, APPIUM_URL


class TestsCreateTask(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(
            command_executor=APPIUM_URL,
            desired_capabilities=DESIRED_CAPABILITIES
        )

    def test_open_new_task(self) -> None:
        page = NewTaskPage(self.driver)
        page.open_page_new_task()

        self.assertEqual(page.page_title_new_task(), "New Task")

    def tearDown(self) -> None:
        self.driver.quit()
