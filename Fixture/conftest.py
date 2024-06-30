import time
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options


@pytest.fixture(scope="module")
def driver_setup(request):
    capabilities = UiAutomator2Options().load_capabilities({
     "platformName": "Android",
     "appium:deviceName": "Galaxy A32",
     "appium:udid": "RF9R305PJ1W",
     "appium:automationName": "UiAutomator2",
     "appium:noReset": "true",
     "appium:newCommandTimeout": 3000,
     "appium:platformVersion": "12",
     "appium:appPackage": "com.oliveyoung",
     "appium:appActivity": "com.oliveyoung.presentation.home.MainActivity"
    })
    driver = webdriver.Remote(command_executor="http://localhost:4723", options=capabilities)
    request.cls.driver = driver
    yield
    time.sleep(4)
    driver.terminate_app("com.oliveyoung")
    driver.quit()
