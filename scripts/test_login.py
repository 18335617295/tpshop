import time

import pytest

from base.find_toast import find_toast
from base.base_analyze import analyze_file
from base.base_driver import init_driver

from page.page import Page


class TestLogin():
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(2)
        self.driver.quit()

    @pytest.mark.parametrize("value", analyze_file("login_data.yaml", "test_login"))
    def test_login(self,value):
        # 点击我的
        self.username = value['username']
        self.password = value['password']
        self.expecate = value['expecate']
        print(self.username, self.password, self.expecate)
        self.page.home_page.click_my_button()
        # 点击登录注册
        self.page.my_page.click_login_button()
        self.page.login_page.input_username(self.username)
        self.page.login_page.input_passwodr(self.password)
        self.page.login_page.click_login()
        assert find_toast(self.driver, self.expecate)
