class BasePage:
    def __init__(self, page):
        self.page = page
        self.sign_in_btn = ".header-actions__item.header-actions__item--user"

    def get_locator(self, locator):
        return self.page.locator(locator)

    def wait_for_selector(self, selector, state="visible"):
        return self.page.wait_for_selector(selector, state=state)


