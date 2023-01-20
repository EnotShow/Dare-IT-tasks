from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class Dashboard(BasePage):
    main_page_button_xpath = '//*[@id="__next"]/div[1]/div/div/div/ul[1]/div[1]/div[2]/span'
    players_button_xpath = '//*[@id="__next"]/div[1]/div/div/div/ul[1]/div[2]/div[2]/span'
    language_button_xpath = '//*[@id="__next"]/div[1]/div/div/div/ul[2]/div[1]/div[2]/span'
    sign_out_button_xpath = '//*[@id="__next"]/div[1]/div/div/div/ul[2]/div[2]/div[2]/span'
    dev_team_contact_button_xpath = '//*[@id="__next"]/div[1]/main/div[3]/div[1]/div/div[3]/a'
    add_player_button_xpath = '//*[@id="__next"]/div[1]/main/div[3]/div[2]/div/div/a/button'

    last_created_player = '//*[@id="__next"]/div[1]/main/div[3]/div[3]/div/div/a[1]/button'
    last_updated_player = '//*[@id="__next"]/div[1]/main/div[3]/div[3]/div/div/a[2]/button'
    last_created_match = '//*[@id="__next"]/div[1]/main/div[3]/div[3]/div/div/a[3]/button'
    last_updated_match = '//*[@id="__next"]/div[1]/main/div[3]/div[3]/div/div/a[4]/button'
    last_updated_report = '//*[@id="__next"]/div[1]/main/div[3]/div[3]/div/div/a[5]/button'

    def click_on_main_page_button(self):
        self.driver.find_element(By.XPATH, self.main_page_button_xpath).click()
