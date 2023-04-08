from appium.webdriver.common.appiumby import AppiumBy


class TaskMenuLocators:
    BUTTON_DELETE: tuple = (
        AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                        "/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view."
                        "View[1]/android.view.View[2]/android.widget.Button"
    )
