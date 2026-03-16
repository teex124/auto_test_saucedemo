from pages import *



def test_successful_order(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    login_page.open()
    login_page.login()
    inventory_page.add_product_in_cart('Sauce Labs Backpack')
    inventory_page.open_cart()
    cart_page.check_new_product_in_cart('Sauce Labs Backpack')


