# -*- coding: utf-8 -*-
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from app.backend.facebook.tech_params import EMAIL_FIELD, \
    PASSWORD_FIELD, SUBMIT_BUTTON
from app.backend.config import FACEBOOK_LOGIN, FACEBOOK_PASSWORD
from app.backend.facebook.facebook_homepage import FacebookHomepage


class FacebookAuthenticate(FacebookHomepage):
    def __init__(self):
        super(FacebookAuthenticate, self).__init__()
        self.wait = WebDriverWait(self.driver, 5)
        self.login_field = None
        self.pass_field = None
        self.submit_button = None

    def facebook_authenticate(self):
        self.find_login_and_password_fields()
        self.send_credentials()
        self.find_and_click_on_submit_button()

    def find_login_and_password_fields(self):
        login_selector = EMAIL_FIELD[0]
        login_value = EMAIL_FIELD[1]
        pass_selector = PASSWORD_FIELD[0]
        pass_value = PASSWORD_FIELD[1]
        self.login_field = self.driver.find_element(
            login_selector, login_value
        )
        self.pass_field = self.driver.find_element(
            pass_selector, pass_value
        )

    def send_credentials(self):
        self.login_field.send_keys(FACEBOOK_LOGIN)
        self.pass_field.send_keys(FACEBOOK_PASSWORD)

    def find_and_click_on_submit_button(self):
        self.submit_button = self.wait.until(
            EC.element_to_be_clickable(
                SUBMIT_BUTTON
            )
        )
        self.submit_button.click()


if __name__ == "__main__":
    o = FacebookAuthenticate()
    o.open_home_page()
    o.facebook_authenticate()