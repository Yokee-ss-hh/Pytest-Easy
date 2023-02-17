import pytest
from pages.login_page import LoginPage
from utilities.data_file import TestData
import logging


@pytest.mark.usefixtures()
class TestLogin:
    log_info = logging.getLogger()
    log_info.setLevel(logging.INFO)

    @pytest.mark.skip
    @pytest.fixture(params=TestData.test_sheet_data("login"))
    def get_data(self,request):
        return request.param

    def test_verify_web_page(self, get_data):
        obj_tlp = LoginPage(self.driver)

        try:
            self.log_info.info("Navigated to the demoqa website")
            if obj_tlp.get_title() == get_data["TC01"]["title"]:
                self.log_info.info("Verified page title")
                return True
            else:
                return False

        except Exception as e:
            self.log_info.exception(f"test_login_user method is failed : {e.args}")

