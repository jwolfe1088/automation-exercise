import pytest
import os

BASE_URL = "https://www.automationexercise.com"
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

def test_login_valid_credentials(home_page, login_page):
    home_page.navigate_to_home()
    home_page.click_login()
    login_page.login(EMAIL, PASSWORD)
    assert login_page.page.url == "https://www.automationexercise.com/"

def test_login_invalid_credentials(home_page, login_page):
    home_page.navigate_to_home()
    home_page.click_login()
    login_page.login(EMAIL, "wrong_password")
    assert login_page.get_error_message() == "Your email or password is incorrect!"

def test_login_empty_fields(home_page, login_page):
    home_page.navigate_to_home()
    home_page.click_login()
    login_page.login("", "")
    assert login_page.page.url == "https://www.automationexercise.com/login"

def test_register_new_user(home_page, login_page):
    home_page.navigate_to_home()
    home_page.click_login()
    login_page.register("Jon", "something_different111010@gmail.com")
    assert login_page.page.url == "https://www.automationexercise.com/signup"
