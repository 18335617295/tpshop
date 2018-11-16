from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class HomePage(BaseAction):
    my_button = By.XPATH, "//*[@text='我的' and @resource-id='com.tpshop.malls:id/tab_txtv']"

    def click_my_button(self):
        self.click(self.my_button)
