git remote add origin https://github.com/shox1192/qa_automation_PET.git
git branch -M main
git push -u origin main
__(self, page):
        super().__init__(page)
        self.name_field = "//input[@formcontrolname='name']"
        self.surname_field = "//input[@formcontrolname='surname']"
        self.phone_number_field = "//input[@formcontrolname='phone']"
        self.email_field = "//input[@formcontrolname='email']"
        self.password_field = "//input[@formcontrolname='password']"
        self.submit_registration_btn = ".button--green.auth-modal__submit"
        self.phone_validation_modal = ".auth-modal__form.ng-untouched"

    def fill_registration_fields_and_submit(self):
        self.page.fill(self.name_field, self.random_cyrillic_string(7))
        self.page.fill(self.surname_field, self.random_cyrillic_string(8))
        self.page.fill(self.phone_number_field, "093" + self.random_valid_phone())
        self.page.fill(self.email_field, self.random_string(7) + "@box.com")
        self.page.fill(self.password_field, "123Qweasd")
        self.page.locator(self.submit_registration_btn).click(force=True)

    def get_phone_validation_modal_window(self):
        self.page.locator(self.phone_validation_modal).wait_for(timeout=5000)
        return self.get_locator(self.phone_validation_modal)

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
        random_string = "".join(random.choice(alphabet) for each in range(amount_of_chars))
        return random_string
