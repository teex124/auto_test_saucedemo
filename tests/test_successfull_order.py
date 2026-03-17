from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.test_data import TestData


def test_successful_order(page, block_images):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    login_page.open()
    login_page.login(login=TestData.LOGIN, password=TestData.PASSWORD)
    inventory_page.add_product_in_cart('Sauce Labs Backpack')
    inventory_page.open_cart()
    cart_page.check_new_product_in_cart('Sauce Labs Backpack')


