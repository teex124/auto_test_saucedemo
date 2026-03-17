from pages.base_page import BasePage
from locators.login_locators import LoginLocators
from utilits.test_data import TestData


class LoginPage(BasePage):
    url = 'https://www.saucedemo.com/'
    def login(self):
        self.fill(LoginLocators.LOGIN_INPUT, TestData.LOGIN)
        self.fill(LoginLocators.PASSWORD_INPUT, TestData.PASSWORD)
        self.click(LoginLocators.LOGIN_BUTTON)

