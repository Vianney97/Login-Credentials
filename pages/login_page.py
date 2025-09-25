from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.email_input = "#user_email"
        self.password_input = "#user_password"
        self.login_button = "input[name='commit']"

    def goto(self, url: str):
        self.page.goto(url)


    def login(self, email: str, password: str):
        self.page.fill(self.email_input, email)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)
        self.page.wait_for_load_state("networkidle") 