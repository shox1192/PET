class BasePage:
    def __init__(self, page):
        self.page = page

    def get_locator(self, locator):
        return self.page.locator(locator)

    def wait_for_selector(self, selector, state="visible"):
        return self.page.wait_for_selector(selector, state=state)


