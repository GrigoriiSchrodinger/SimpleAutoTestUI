import unittest

from appium import webdriver

from src.page.CatalogPage import CatalogPage
from src.page.WelcomePage import WelcomePage


class TestsApp(unittest.TestCase):
    URL = "http://127.0.0.1:4723"

    def setUp(self) -> None:
        desired_capabilities = {
            "platformName": "Android",
            "platformVersion": "13",
            "deviceName": "Pixel 6 Pro",
            "automationName": "uiautomator2",
            "app": "/Users/schrodinger/main/SimpleAutoTestUI/src/app.apk",
        }
        self.driver = webdriver.Remote(command_executor=self.URL, optiocns=desired_capabilities)

    def test_one(self) -> None:
        page = CatalogPage(self.driver)

        page.open_catalog_page()
        page.add_code_smell()

    def tearDown(self) -> None:
        self.driver.quit()
