import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class CartPageClass:

    def __init__(self, driver):
        self.driver = driver


        # 장바구니 첫번째 상품 클릭
        self.close_btn = "/hierarchy/android.widget.FrameLayout/android.widget." \
                         "LinearLayout/android.widget.FrameLayout/android.widget." \
                         "LinearLayout/android.widget.FrameLayout/android.widget." \
                         "RelativeLayout/android.webkit.WebView/android.webkit." \
                         "WebView/android.view.View/android.view.View/android.widget.Button[2]"
