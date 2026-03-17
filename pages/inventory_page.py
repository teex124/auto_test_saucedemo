from pages.base_page import BasePage
from locators.inventory_locators import InventoryLocators
import re

class InventoryPage(BasePage):
    url = 'https://www.saucedemo.com/inventory.html'
    def add_product_in_cart(self, product_name: str):
        product = self.page.locator(InventoryLocators.CARD, has_text=product_name)
        product.locator('button').click()
    def open_cart(self):
        self.click(InventoryLocators.CART)
