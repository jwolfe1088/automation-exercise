import pytest

BASE_URL = "https://www.automationexercise.com"


def test_products_page_loads(home_page, products_page):
    home_page.navigate_to_home()
    home_page.click_products()
    assert products_page.page.url == "https://www.automationexercise.com/products"

def test_search_product(home_page, products_page):
    home_page.navigate_to_home()
    home_page.click_products()
    products_page.search_products("Blue Top")
    assert products_page.get_product_count() > 0

def test_filter_by_category(home_page, products_page):
    home_page.navigate_to_home()
    home_page.click_products()
    products_page.filter_by_category("1")
    assert products_page.get_product_count() > 0
    assert products_page.page.url == "https://www.automationexercise.com/category_products/1"

def test_product_count_greater_than_zero(home_page, products_page):
    home_page.navigate_to_home()
    home_page.click_products()
    assert products_page.get_product_count() > 0

