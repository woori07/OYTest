import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BottomSeat:

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

        # 장바구니 첫번째 상품 클릭
        self.close_btn = "/hierarchy/android.widget.FrameLayout/android.widget." \
                         "LinearLayout/android.widget.FrameLayout/android.widget." \
                         "LinearLayout/android.widget.FrameLayout/android.widget." \
                         "RelativeLayout/android.webkit.WebView/android.webkit." \
                         "WebView/android.view.View/android.view.View/android.widget.Button[2]"



    # 상품 클릭 함수


    # 장바구니 클릭 함수


    # 팝업 뜨는지 체크하는 함수


    # 장바구니 이동 클릭 함수


    # 상품명 파싱하는 함수
        # return 상품명







    def check_and_click_popup(self):
        try:
            # 버튼이 나타날 때까지 기다림
            wait = WebDriverWait(self.driver, 12)
            button_element = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, self.close_btn)))

            # 버튼 클릭
            button_element.click()
            print("버튼을 클릭했습니다.")
            time.sleep(2)
            return False

        except TimeoutException:
            print("버튼을 찾지 못했습니다. 시간 초과.")
            return True
        except Exception as e:
            print(f"버튼 클릭 중 오류 발생: {e}")
            return False
