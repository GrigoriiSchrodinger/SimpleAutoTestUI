from appium.webdriver.common.appiumby import AppiumBy


class ListTaskLocators:
    BUTTON_ADD_TASK: tuple = (
        AppiumBy.ACCESSIBILITY_ID, "New Task"
    )



