from appium.webdriver.common.appiumby import AppiumBy


class NewTaskLocators:
    TITLE_PAGE: tuple = (
        AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
                        "androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view."
                        "View[1]/android.widget.TextView"
    )
    FIELD_NAME_TASK: tuple = (
        AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
                        "androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/"
                        "android.widget.ScrollView/android.widget.EditText[1]"
    )
    FIELD_DESCRIPRION_TASK: tuple = (
        AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
                        "androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget."
                        "ScrollView/android.widget.EditText[2]"
    )
    BUTTON_SAVE_TASK: tuple = (
        AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
                        "androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/"
                        "android.view.View[2]/android.widget.Button"
    )
    NOTICE_WARNING: tuple = (
        AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
                        "androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view."
                        "View[2]/android.view.View/android.widget.TextView"
    )

