from pages.base_page import BasePage


LOGIN = 'standard_user'
PASSWORD = 'secret_sauce'

LOGIN_INPUT = '#user-name'
PASSWORD_INPUT = '#password'
LOGIN_BUTTON = '#login-button'

class LoginPage(BasePage):
    url = 'https://www.saucedemo.com/'
    def login(self):
        self.page.locator(LOGIN_INPUT).fill(LOGIN)
        self.page.locator(PASSWORD_INPUT).fill(PASSWORD)
        self.page.locator(LOGIN_BUTTON).click()

