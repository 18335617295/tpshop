from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MyPage(BaseAction):
    login_button = By.XPATH, "//*[@text='登录/注册']"

    def click_login_button(self):
        self.click(self.login_button)
