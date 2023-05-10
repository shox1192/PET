import pytest
from tests.base_test import BaseTest
from playwright.sync_api import expect
from pages.main_page.page_main import HomePage
from pages.page_login.login_page import LoginPage

"""
This class contains the UI tests of the log in flow!
"""

class TestLogin(BaseTest):
    @pytest.fixture(autouse=True)
    def setup_class(self):
        self.open_page()

    def test_login_success(self):
        HomePage(self.page).open_login_popup()
        LoginPage(self.page).fill_login_form_and_submit()