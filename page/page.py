from page.home_page import HomePage
from page.login_page import LoginPage
from page.my_page import MyPage


class Page(object):
    def __init__(self, driver):
        self.driver = driver

    @property
    def my_page(self):
        return MyPage(self.driver)

    @property
    def home_page(self):
        return HomePage(self.driver)

    @property
    def login_page(self):
        return LoginPage(self.driver)