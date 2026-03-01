from pages.base_page import Basepage

class ProductsPage(Basepage):
    def __init__(self, page):
        super().__init__(page)

    def search_products(self, product_name):
        self.page.fill("input[id='search_product']", product_name)
        self.page.click("button[id='submit_search']")

    def add_first_item(self):
        self.page.locator(".btn.btn-default.add-to-cart").first.click()

    def get_product_count(self):
        return self.page.locator(".product-image-wrapper").count()
    
    def click_first_product(self):
        self.page.locator(".product-image-wrapper").first.click()

    def filter_by_category(self, category_url):
        self.page.goto(f"https://www.automationexercise.com/category_products/{category_url}")