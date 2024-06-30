import pytest
from dummyfile.firstpopupTC.first_popup_page import BottomSeat


@pytest.mark.usefixtures("driver_setup")
class TestFirst:
    def test_popup_close(self):
        # 인스턴스화
        # 파싱값 담을 배열2개 선언

        # 첫번째 상품명 파싱 - utils/parsing_func
        # 파싱한 값 배열에 담기 -
        # 상품 클릭
        # 장바구니 담기 클릭
        # 팝업 뜨는지 체크
        # 장바구니 이동 클릭 -
        # 장바구니 상품명 파싱 - utils/parsing_func



        bottomseat = BottomSeat(self.driver)
        bottomseat.check_and_click_popup()

        # 두개의 값이 일치하는지 확인
        assert bottomseat.check_and_click_popup(), "Popup test failed!"
