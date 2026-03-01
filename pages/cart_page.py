from pages.base_page import Basepage

class CartPage(Basepage):
    def __init__(self, page):
        super().__init__(page)

    def get_cart_items(self):
        count = self.page.locator("tr[id^='product-']").count()
        print(f"Cart items count: {count}")
        return count

    def remove_first_item(self):
        self.page.locator("a.cart_quantity_delete").first.click()
        self.page.wait_for_load_state("networkidle")

    def click_proceed_to_checkout(self):
        self.page.click("a:has-text('Proceed To Checkout')")

    def get_total_price(self):
        return self.page.inner_text("td.cart_total p")

    def click_view_cart_from_popup(self):
        self.page.locator("#cartModal a[href='/view_cart']").click()