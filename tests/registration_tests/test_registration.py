from tests.base_test import BaseTest
from playwright.sync_api import expect
from pages.main_page.page_main import HomePage
from pages.registration_page.page_registration import RegistrationPage
import pytest

class TestRegistration(BaseTest):
    @pytest.fixture(autouse=True)
    def setup_class(self):
        self.open_page()

    def test_registration_till_phone_validation_pop_up(self):
        HomePage(self.page).open_registration_popup()
        RegistrationPage(self.page).fill_registration_fields_and_submit()
        expect(
            RegistrationPage(self.page).get_phone_validation_modal_window()
        ).to_be_visible()
        expect(
            RegistrationPage(self.page).get_phone_validation_modal_window()
        ).to_have_text("Підтвердження номера телефону Для реєстрації введіть "
                       "код підтвердження із SMS або Viber, надісланого на номер  Телефон  "
                       "Код підтвердження  Підтвердити  Відправити код ще раз  (60) ")

    @pytest.mark.parametrize(
        "form, message",

    )
    def test_forms_validation(self, form, message):
