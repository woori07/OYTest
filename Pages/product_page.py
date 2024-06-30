import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class ProductPageClass:

    def __init__(self, driver):
        self.driver = driver


        # 장바구니 담기 버튼
        self.close_btn = "/hierarchy/android.widget.FrameLayout/android.widget." \
                         "LinearLayout/android.widget.FrameLayout/android.widget." \
                         "LinearLayout/android.widget.FrameLayout/android.widget." \
                         "RelativeLayout/android.webkit.WebView/android.webkit." \
                         "WebView/android.view.View/android.view.View/android.widget.Button[2]"


        # 담기 완료 팝업
        self.close_btn = "/hierarchy/android.widget.FrameLayout/android.widget." \
                         "LinearLayout/android.widget.FrameLayout/android.widget." \
                         "LinearLayout/android.widget.FrameLayout/android.widget." \
                         "RelativeLayout/android.webkit.WebView/android.webkit." \
                         "WebView/android.view.View/android.view.View/android.widget.Button[2]"


        # 장바구니 이동 버튼
        self.close_btn = "/hierarchy/android.widget.FrameLayout/android.widget." \
                         "LinearLayout/android.widget.FrameLayout/android.widget." \
                         "LinearLayout/android.widget.FrameLayout/android.widget." \
                         "RelativeLayout/android.webkit.WebView/android.webkit." \
                         "WebView/android.view.View/android.view.View/android.widget.Button[2]"




        # 장바구니 클릭 함수


        # 팝업 뜨는지 체크하는 함수


        # 장바구니 이동 클릭 함수
