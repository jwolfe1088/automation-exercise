from pages.base_page import Basepage

class LoginPage(Basepage):
    def __init__(self, page):
        super().__init__(page)

    def login(self, email, password):
        self.page.fill("input[data-qa='login-email']", email)
        self.page.fill("input[data-qa='login-password']", password)
        self.page.click("button[data-qa='login-button']")

    def register(self, name, email):
        self.page.fill("input[data-qa='signup-name']", name)
        self.page.fill("input[data-qa='signup-email']", email)
        self.page.click("button[data-qa='signup-button']")

    def get_error_message(self):
        return self.page.inner_text("p:has-text('Your email or password is incorrect')")