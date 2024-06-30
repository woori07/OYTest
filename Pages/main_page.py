import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class MainPageClass:

    def __init__(self, driver):
        self.driver = driver



        # 첫번째 상품
        self.close_btn = "/hierarchy/android.widget.FrameLayout/android.widget." \
                         "LinearLayout/android.widget.FrameLayout/android.widget." \
                         "LinearLayout/android.widget.FrameLayout/android.view." \
                         "ViewGroup/android.view.ViewGroup[1]/android.view." \
                         "ViewGroup/android.webkit.WebView/android.webkit." \
                         "WebView/android.view.View/android.view.View/android." \
                         "view.View/android.view.View[2]/android.view.View[2]/android." \
                         "view.View/android.view.View[1]/android.view.View/android.view." \
                         "View[4]/android.view.View[2]/android.view.View/android.view." \
                         "View/android.view.View[1]"






        # 상품 클릭 함수

