import random
import string
import os

from pages.base_page import BasePage

"""
The class which represents the Registration Page of the website with all the locators, 
selectors and all necessary functions and methods for this exact page.
"""

class RegistrationPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.name_field = "//input[@formcontrolname='name']"
        self.surname_field = "//input[@formcontrolname='surname']"
        self.phone_number_field = "//input[@formcontrolname='phone']"
        self.email_field = "//input[@formcontrolname='email']"
        self.password_field = "//input[@formcontrolname='password']"
        self.submit_registration_btn = ".button--green.auth-modal__submit"
        self.phone_validation_modal = ".auth-modal__form.ng-untouched"
        self.first_name_field_validation_msg = "(//p[@class='validation-message ng-star-inserted'])[1]"
        self.last_name_field_validation_msg = "(//form-error[@class='validation-message'])[2]"
        self.wrong_phone_validation_msg = "(//form-error[@class='validation-message'])[3]"
        self.wrong_email_validation_msg = "(//form-error[@class='validation-message'])[4]"
        self.registration_modal = ".modal__holder.modal__holder_show_animation"
        self.password_less_than_6 = "(//p[@class='errors-list__text'])[3]"
        self.password_no_cyrillic_chars = "(//p[@class='errors-list__text'])[2]"
        self.password_no_digits = "(//p[@class='errors-list__text'])[4]"
        self.password_no_upcase = "(//p[@class='errors-list__text'])[5]"

    def fill_registration_fields_and_submit(self):
        self.page.fill(self.name_field, self.random_cyrillic_string(7))
        self.page.fill(self.surname_field, self.random_cyrillic_string(8))
        self.page.fill(self.phone_number_field, "093" + self.random_valid_phone())
        self.page.fill(self.email_field, self.random_string(7) + "@box.com")
        self.page.fill(self.password_field, os.getenv("PASSWORD"))
        self.page.locator(self.submit_registration_btn).click(force=True)

    def fill_invalid_name(self, form):
        if form == "name":
            locator = self.name_field
        else:
            locator = self.surname_field
        self.page.fill(locator, self.random_string(7))

    def fill_invalid_phone_number(self):
        self.page.fill(self.phone_number_field, "123")

    def fill_invalid_email(self):
        self.page.fill(self.email_field, "wrongemail")

    def fill_invalid_password(self, password):
        self.page.fill(self.password_field, password)

    def pick_the_correct_invalid_password_message_locator(self, password):
        if password == "1Qwer":
            locator = self.password_less_than_6
        elif password == "пароль":
            locator = self.password_no_cyrillic_chars
        elif password == "noDigits":
            locator = self.password_no_digits
        elif password == "noupcase1":
            locator = self.password_no_upcase
        else:
            locator = ""
        return self.get_locator(locator)


    def get_phone_validation_modal_window(self):
        self.page.locator(self.phone_validation_modal).wait_for(timeout=5000)
        return self.get_locator(self.phone_validation_modal)

    def get_registration_validation_message(self, form):
        if form == "name":
            locator = self.first_name_field_validation_msg
        else:
            locator = self.last_name_field_validation_msg
        return self.get_locator(locator)

    def get_invalid_phone_validation_message(self):
        return self.get_locator(self.wrong_phone_validation_msg)

    def get_invalid_email_validation_message(self):
        return self.get_locator(self.wrong_email_validation_msg)

    def get_registration_modal(self):
        return self.get_locator(self.registration_modal)

    def random_valid_phone(self):
        phone = random.randint(0000000, 9999999)
        return str(phone)

    def random_string(self, amount_of_chars):
        rand_string = "".join(random.choice(string.ascii_lowercase) for _ in range(amount_of_chars))
        return rand_string

    @staticmethod
    def random_cyrillic_string(amount_of_chars):
        """
        It is necessary for the first name and last name,
        as validation for them requires cyryllic letters!
        """

        alphabet = ["а", "б", "в", "г", "ґ", "д", "е", "є",
                    "ж", "з", "и", "і", "ї", "й", "к", "л",
                    "м", "н", "о", "п", "р", "с", "т", "у",
                    "ф", "х", "ц", "ч", "ш", "щ", "ь", "ю", "я"]
        random_string = "".join(random.choice(alphabet) for _ in range(amount_of_chars))
        return random_string
