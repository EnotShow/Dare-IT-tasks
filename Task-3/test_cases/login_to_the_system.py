import os
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import IMPLICITLY_WAIT


class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        # self.driver.fullscreen_window()
        # self.driver.implicitly_wait(IMPLICITLY_WAIT)

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_login_to_the_system(self):
        user_login = LoginPage(self.driver)
        dashboard = Dashboard(self.driver)

        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.submit_sign_in_button()
        dashboard.title_of_page()

