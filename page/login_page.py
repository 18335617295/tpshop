from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class LoginPage(BaseAction):
    username = By.XPATH, "//*[@text='请输入手机号码']"
    password = By.XPATH, "//*[@index='4']"
    login_button = By.XPATH, "//*[@index='7']"

    def input_username(self, text):
        self.input(self.username, text)

    def input_passwodr(self, text):
        self.input(self.password, text)

    def click_login(self):
        self.click(self.login_button)
