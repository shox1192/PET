import os
import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

class BaseTest:
    load_dotenv()

    def choose_browser(self, page):
        browser = ""
        headless = False
        browser_name = os.getenv("BROWSER")
        if browser_name == "Chrome":
            browser = page.chromium.launch(channel="chrome", headless=headless)
        elif browser_name == "Safari":
            browser = page.webkit.launch(headless=headless)
        elif browser_name == "Firefox":
            browser = page.firefox.launch(headless=headless)
        elif browser_name == "Edge":
            browser = page.chromium.launch(channel="msedge", headless=headless)
        return browser

    def choose_device(self, page):
        device_name = os.getenv("DEVICE")
        if os.getenv("DEVICE") != "DESKTOP":
            devices = page.devices[device_name]
        else:
            devices = "DESKTOP"
        return devices

    @pytest.fixture(autouse=True)
    def run_before_tests(self):
        with sync_playwright() as p:
            self.generate_page(p)
            yield self.page

    def generate_page(self, page):
        devices = self.choose_device(page)
        browser = self.choose_browser(page)
        if devices == "DESKTOP":
            context = page.chromium.launch(
                channel="chrome", headless=False # TODO: True
            ).new_context()
        else:
            context = browser.new_context(**devices)
        self.page = context.new_page()
        return self.page

    def open_page(self):
        self.url = "https://rozetka.com.ua/ua/"
        self.page.goto(self.url, timeout=300000)
        self.page.wait_for_load_state(state="load", timeout=20000)

    # def set_local_storage(self, site_name, value):
    #     if value:
    #         dev_url = ""
    #         self.page.evaluate_handle(
    #             f"window.localStorage.setItem('api-url', '{dev_url}');"
    #         )
    #         self.page.reload()
