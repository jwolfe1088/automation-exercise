import pytest

def test_cart_page_loads(home_page, cart_page):
    home_page.navigate_to_home()
    home_page.click_cart()
    assert cart_page.page.url == "https://www.automationexercise.com/view_cart"

def  test_add_item_to_cart(home_page, products_page, cart_page):
    home_page.navigate_to_home()
    home_page.click_products()
    products_page.add_first_item()
    cart_page.click_view_cart_from_popup()
    assert cart_page.get_cart_items() == 1

def test_remove_item_from_cart(home_page, products_page, cart_page):
    home_page.navigate_to_home()
    home_page.click_products()
    products_page.add_first_item()
    cart_page.click_view_cart_from_popup()
    cart_page.remove_first_item()
    assert cart_page.get_cart_items() == 0

    
