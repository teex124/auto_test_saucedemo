from pages.base_page import BasePage
from playwright.sync_api import expect

CARD = '.inventory_item_description'
CART = '.shopping_cart_link'

class InventoryPage(BasePage):
    url = 'https://www.saucedemo.com/inventory.html'
    def add_product_in_cart(self, product_name: str):
        product = self.page.locator(CARD, has_text=product_name)
        product.locator('button').click()
    def open_cart(self):
        self.page.locator(CART).click()
