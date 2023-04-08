import json
import os
from dotenv import load_dotenv

load_dotenv()

with open('settings.json') as settings:
    settings = json.load(settings)

# appium server settings
APPIUM_HOST = os.environ.get("APPIUM_HOST", "127.0.0.1")
APPIUM_PORT = os.environ.get("APPIUM_PORT", "4723")
APPIUM_URL = f'http://{APPIUM_HOST}:{APPIUM_PORT}'

# device settings
DESIRED_CAPABILITIES = dict(
    platformName=os.environ.get("OS", "Android"),
    platformVersion=os.environ.get("VERSION"),
    deviceName=os.environ.get("NAME_DEVICE"),
    automationName=os.environ.get("AUTOMATION_NAME", "uiautomator2"),
    app=settings["path_app"],
)
# appium driver settings
IMPLICIT_WAIT = 30


