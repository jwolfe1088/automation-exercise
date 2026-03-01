from pages.base_page import Basepage

BASE_URL = "https://www.automationexercise.com"

class HomePage(Basepage):
    def __init__(self, page):
        super().__init__(page)

    def dismiss_popup(self):
        try:
            self.page.locator(".fc-close").click(timeout=3000)
        except:
            pass

    def navigate_to_home(self):
        self.page.goto(BASE_URL)
        
    def click_login(self):
        self.page.click("a[href='/login']")

    def click_products(self):
        self.page.goto("https://www.automationexercise.com/products")

    def click_cart(self):
        self.page.click("a[href='/view_cart']")

    