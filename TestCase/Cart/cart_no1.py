import pytest
from dummyfile.firstpopupTC.first_popup_page import BottomSeat
from Pages.main_page import MainPageClass
from Pages.product_page import ProductPageClass
from Pages.cart_page import CartPageClass


@pytest.mark.usefixtures("driver_setup")
class TestFirst:
    # 나의 장바구니에 담았어요" 메시지 출력 확인
    def test_add_cart_alert(self, driver_setup):
        self.driver = driver_setup

        # 인스턴스화 main_page.py, product_page.py, utils/parsing_func.py, cart_page.py
        main_page_instance = MainPageClass(self.driver)
        product_page_instance = ProductPageClass(self.driver)

        # 파싱값 담을 배열2개 선언

        # 상품 클릭 - main_page.py
        main_page_instance.click_first_product()
        # 상품상세 상품명 파싱 - product_page.py, utils/parsing_func.py
        text_value1 = product_page_instance.get_element_text()
        print(text_value1)
        # 장바구니 담기 클릭 - product_page.py
        product_page_instance.click_add_to_cart()

        # 팝업 뜨는지 체크 - product_page.py
        assert product_page_instance.is_add_popup_displayed(), "Popup not displayed!"

        # 장바구니 이동 클릭 - product_page.py
        # 장바구니 상품명 파싱 - cart_page.py, utils/parsing_func


        # 두개의 값이 일치하는지 확인
        # assert text_value1 == '[종석 Pick]다슈 포맨 밤부 포레스트 메가 하드 스프레이 180ml', "Popup test failed!"
