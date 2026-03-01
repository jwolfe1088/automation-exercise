from pages.base_page import Basepage

class CheckoutPage(Basepage):
    def __init__(self, page):
        super().__init__(page)

    def enter_comment(self, comment):
        self.page.fill("textarea[name='message']", comment)

    def click_place_order(self):
        self.page.click("a:has-text('Place Order')")

    def enter_payment_details(self, name, card_number, cvc, expiry_month, expiry_year):
        self.page.fill("input[data-qa='name-on-card']", name)
        self.page.fill("input[data-qa='card-number']", card_number)
        self.page.fill("input[data-qa='cvc']", cvc)
        self.page.fill("input[data-qa='expiry-month']", expiry_month)
        self.page.fill("input[data-qa='expiry-year']", expiry_year)

    def click_confirm_order(self):
        self.page.click("button[data-qa='pay-button']")

    def get_success_message(self):
        return self.page.inner_text("h2[data-qa='order-placed']")
