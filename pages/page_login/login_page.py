import os
import time
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.email_input_login = "[id='auth_email']"
        self.password_input_login = "[id='auth_pass']"
        self.captcha_checkbox = "[id='recaptcha-anchor']"
        self.submit_login = ".button--large.button--green"

    def fill_login_form_and_submit(self):
        self.page.fill(self.email_input_login, os.getenv("USER_EMAIL"))
        self.page.fill(self.password_input_login, os.getenv("PASSWORD"))
        self.get_locator(self.submit_login).click()
        time.sleep(3)
        self.get_locator(self.captcha_checkbox).click(force=True)
        self.get_locator(self.submit_login).click()

