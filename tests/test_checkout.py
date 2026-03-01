import pytest
import os

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

def test_checkout_flow(login_page, home_page, products_page, cart_page, checkout_page):
    home_page.navigate_to_home()
    home_page.click_login()
    login_page.login(EMAIL, PASSWORD)
    home_page.click_products()
    products_page.add_first_item()
    cart_page.click_view_cart_from_popup()
    cart_page.click_proceed_to_checkout()
    checkout_page.enter_comment("Make it snappy!")
    checkout_page.click_place_order()
    checkout_page.enter_payment_details("Jon", "123456677800", "123", "01", "2030")
    checkout_page.click_confirm_order()
    assert "ORDER PLACED!" in checkout_page.get_success_message()



