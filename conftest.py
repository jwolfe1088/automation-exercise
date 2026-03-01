import os
import pytest
from dotenv import load_dotenv
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

load_dotenv()

@pytest.fixture
def home_page(page):
    return HomePage(page)

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def products_page(page):
    return ProductsPage(page)

@pytest.fixture
def cart_page(page):
    return CartPage(page)

@pytest.fixture
def checkout_page(page):
    return CheckoutPage(page)