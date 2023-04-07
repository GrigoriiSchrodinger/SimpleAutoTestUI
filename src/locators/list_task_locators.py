from appium.webdriver.common.appiumby import AppiumBy


class ListTaskLocators:
    BUTTON_ADD_TASK: tuple = (
        AppiumBy.ACCESSIBILITY_ID, "New Task"
    )
    NOTICE_ADD_TASK: tuple = (
        AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
                        "androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view."
                        "View[3]/android.view.View/android.widget.TextView"
    )




