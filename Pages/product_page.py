import time
import pyautogui
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class ProductPageClass:

    def __init__(self, driver):
        self.driver = driver

        # 장바구니 담기 버튼
        self.add_to_cart = "/hierarchy/android.widget.FrameLayout/android.widget" \
                           ".LinearLayout/android.widget.FrameLayout/android.widget" \
                           ".LinearLayout/android.widget.FrameLayout/android.view.ViewGroup" \
                           "/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView" \
                           "/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]" \
                           "/android.view.View/android.view.View[2]/android.widget.Button[2]"

        # 담기 완료 팝업
        self.add_popup = "//android.widget.Toast[0]"

        # 장바구니 이동 버튼
        self.move_to_cart = '//android.view.View[@content-desc="  장바구니"]"/android.widget.TextView[1]'

        # 현재 페이지의 상품
        self.product_name = "/hierarchy/android.widget.FrameLayout/android.widget" \
                            ".LinearLayout/android.widget.FrameLayout/android.widget" \
                            ".LinearLayout/android.widget.FrameLayout/android.view" \
                            ".ViewGroup/android.view.ViewGroup/android.webkit.WebView" \
                            "/android.webkit.WebView/android.view.View/android.view.View" \
                            "/android.view.View[2]/android.view.View[1]/android.view.View[3]" \
                            "/android.widget.TextView"

    # 장바구니 클릭 함수
    def click_add_to_cart(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((AppiumBy.XPATH, self.add_to_cart)))
        element.click()

    # 팝업 뜨는지 체크하는 함수

    def is_add_popup_displayed(self):
        try:
            # 팝업이 나타날 때까지 기다림 (명시적 대기 시간 10초로 설정)
            imgPath = 'User/'
            wait = WebDriverWait(self.driver, 10)
            popup_element = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, self.add_popup)))
            return True
        except TimeoutException:
            print("팝업이 나타나지 않았습니다. 시간 초과.")
            return False
        except Exception as e:
            print(f"팝업 확인 중 오류 발생: {e}")
            return False

    # 장바구니 이동 클릭 함수

    # 상품명 텍스트 추출 함수
    def get_element_text(self):
        try:
            # 엘리먼트가 나타날 때까지 기다림
            wait = WebDriverWait(self.driver, 14)
            element = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, self.product_name)))

            # 엘리먼트의 텍스트 값 추출
            text_value = element.text
            return text_value
        except TimeoutException:
            print("엘리먼트를 찾지 못했습니다. 시간 초과.")
            return None
        except Exception as e:
            print(f"엘리먼트 텍스트 추출 중 오류 발생: {e}")
            return None
