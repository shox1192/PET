from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.registration_link = ".auth-modal__register-link.button"

    def open_login_popup(self):
        self.get_locator(self.sign_in_btn).click()

    def open_registration_popup(self):
        self.get_locator(self.sign_in_btn).click()
        self.page.locator(self.registration_link).wait_for(state="visible", timeout=10000)
        self.get_locator(self.registration_link).click()



