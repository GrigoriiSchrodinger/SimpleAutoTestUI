# appium server settings
APPIUM_HOST = '127.0.0.1'
APPIUM_PORT = 4723
APPIUM_URL = f'http://{APPIUM_HOST}:{APPIUM_PORT}'

# device settings
DESIRED_CAPABILITIES = dict(
    platformName="Android",
    platformVersion="13",
    deviceName="Pixel 6 Pro",
    automationName="uiautomator2",
    app="/Users/schrodinger/main/SimpleAutoTestUI/src/TODO.apk",
)

# appium driver settings
IMPLICIT_WAIT = 30


