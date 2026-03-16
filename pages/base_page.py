from playwright.sync_api import Page


class BasePage:
    url = None
    def __init__(self, page: Page):
        self.page = page
    def open(self):
        if self.url:
            self.page.goto(self.url)
        else:
            raise 'url не указан'
