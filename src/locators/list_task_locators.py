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
    TASK: tuple = (
        AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                        "/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view."
                        "View[2]/android.view.View[{number_task}]"
    )
    TASK_NAME: tuple = (
        AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                        "/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view."
                        "View[2]/android.view.View[{number_task}]/android.widget.TextView"
    )
    BUTTON_DROP_DOWN_BOX: tuple = (
        AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
                        "androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view."
                        "View[1]/android.view.View[3]/android.widget.Button"
    )
    BUTTON_DROP_DOWN_BOX_REFRESH: tuple = (
        AppiumBy.XPATH, "/hierarchy/android.view.ViewGroup/android.view.View/android.view.View/android.view.View/"
                        "android.widget.ScrollView/android.view.View[2]/android.widget.TextView"
    )





