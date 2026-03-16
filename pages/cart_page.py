from pages.base_page import BasePage
from playwright.sync_api import expect

class CartPage(BasePage):
    url = 'https://www.saucedemo.com/cart.html'

    def check_new_product_in_cart(self, product_name: str):
        expect(self.page.get_by_text(product_name)).to_be_visible()
