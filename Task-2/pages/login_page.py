import selenium
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


# user01@getnada.com pass: Test-1234

class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[@type='submit']"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def submit_sign_in_button(self):
        self.driver.find_element(By.XPATH, self.sign_in_button_xpath).click()
