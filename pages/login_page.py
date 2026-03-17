import re

from pages.base_page import BasePage
from locators.login_locators import LoginLocators
from utils.test_data import TestData


class LoginPage(BasePage):
    url = 'https://www.saucedemo.com/'
    def login(self, login, password):
        self.fill(LoginLocators.LOGIN_INPUT, login)
        self.fill(LoginLocators.PASSWORD_INPUT, password)
        self.click(LoginLocators.LOGIN_BUTTON)

