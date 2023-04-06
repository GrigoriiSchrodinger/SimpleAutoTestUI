import unittest

from appium import webdriver
from src.page.NewTaskPage import NewTaskPage


class TestsApp(unittest.TestCase):
    URL = "http://127.0.0.1:4723"

    def setUp(self) -> None:
        desired_capabilities = {
            "platformName": "Android",
            "platformVersion": "13",
            "deviceName": "Pixel 6 Pro",
            "automationName": "uiautomator2",
            "app": "/Users/schrodinger/main/SimpleAutoTestUI/src/TODO.apk",
        }
        self.driver = webdriver.Remote(command_executor=self.URL, desired_capabilities=desired_capabilities)

    def test_one(self) -> None:
        page = NewTaskPage(self.driver)
        page.open_page_new_task()

        self.assertEqual(page.page_title_new_task(), "New Task")

    def tearDown(self) -> None:
        self.driver.quit()
