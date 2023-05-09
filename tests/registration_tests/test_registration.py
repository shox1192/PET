from tests.base_test import BaseTest
from playwright.sync_api import expect
from pages.main_page.page_main import HomePage
from pages.registration_page.page_registration import RegistrationPage
import pytest

"""
This class contains the UI tests of the registration flow!
"""

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
            RegistrationPage(self.page).get_registration_modal()
        ).to_be_visible()
        expect(
            RegistrationPage(self.page).get_phone_validation_modal_window()
        ).to_have_text(
            "Підтвердження номера телефону Для реєстрації введіть "
            "код підтвердження із SMS або Viber, надісланого на номер  Телефон  "
            "Код підтвердження  Підтвердити  Відправити код ще раз  (60) "
        )
        expect(self.page).to_have_url(self.url)

    @pytest.mark.parametrize(
        "form ,message",
        [
            ["name", "Введіть своє ім'я кирилицею"],
            ["lastname", "Введіть своє прізвище кирилицею"],
        ]
    )
    def test_forms_with_cyrillic_validation(self, form, message):
        HomePage(self.page).open_registration_popup()
        RegistrationPage(self.page).fill_invalid_name(form)
        expect(
            RegistrationPage(self.page).get_registration_validation_message(form)
        ).to_have_text(message)
        expect(
            RegistrationPage(self.page).get_registration_modal()
        ).to_be_visible()
        expect(self.page).to_have_url(self.url)

    def test_registration_with_wrong_phone_number(self):
        HomePage(self.page).open_registration_popup()
        RegistrationPage(self.page).fill_invalid_phone_number()
        expect(
            RegistrationPage(self.page).get_invalid_phone_validation_message()
        ).to_have_text("Введіть номер мобільного телефону")
        expect(
            RegistrationPage(self.page).get_registration_modal()
        ).to_be_visible()
        expect(self.page).to_have_url(self.url)

    def test_registration_with_wrong_email(self):
        HomePage(self.page).open_registration_popup()
        RegistrationPage(self.page).fill_invalid_email()
        expect(
            RegistrationPage(self.page).get_invalid_email_validation_message()
        ).to_have_text(
            "Введіть свою ел. пошту"
        )
        expect(
            RegistrationPage(self.page).get_registration_modal()
        ).to_be_visible()
        expect(self.page).to_have_url(self.url)

    @pytest.mark.parametrize(
        "password, message",
        [
            ["1Qwer", "Не менше 6 символів"],
            ["пароль", "Використовуйте літери латиниці"],
            ["noDigits", "Містити цифри"],
            ["noupcase1", "Містити великі літери"],
        ]
    )
    def test_registration_with_invalid_password(self, password, message):
        HomePage(self.page).open_registration_popup()
        RegistrationPage(self.page).fill_invalid_password(password)
        expect(
            RegistrationPage(self.page).pick_the_correct_invalid_password_message_locator(password=password)
        ).to_have_text(message)
        expect(
            RegistrationPage(self.page).get_registration_modal()
        ).to_be_visible()
        expect(self.page).to_have_url(self.url)

