import unittest

from appium import webdriver
from appium.webdriver.appium_service import AppiumService

from src.page.list_task_page import ListTaskPage
from src.page.task_menu_page import MenuTask
from src.utils.config import APPIUM_URL, DESIRED_CAPABILITIES


class TestDeleteTask(unittest.TestCase):
    def setUp(self):
        self.appium_server = AppiumService()
        self.appium_server.start()
        self.driver = webdriver.Remote(
            command_executor=APPIUM_URL,
            desired_capabilities=DESIRED_CAPABILITIES
        )

    def test_delete_task(self):
        """Проверяем что задача удаляется"""
        page_list_page = ListTaskPage(self.driver)
        page_menu_task = MenuTask(self.driver)
        number_task = 1

        page_list_page.list_task_click_drop_down_box()
        page_list_page.list_task_click_refresh()
        page_list_page.list_task_click_task(number_task=number_task)

        page_menu_task.menu_task_click_delete()

        self.assertIsNot(page_list_page.list_task_return_name_task(number_task=number_task), "Build tower in Pisa")

    def tearDown(self) -> None:
        self.driver.quit()
        self.appium_server.stop()
