from playwright.sync_api import Page


class BasePage:
    url = None
    def __init__(self, page: Page):
        self.page = page

    def open(self):
        if self.url:
            self.page.goto(self.url)
        else:
            raise Exception('url не указан')

    def fill(self, locator, data:str):
        self.page.locator(locator).fill(data)

    def click(self, locator):
        self.page.locator(locator).click()
