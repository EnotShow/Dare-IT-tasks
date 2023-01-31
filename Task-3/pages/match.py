from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class Match(BasePage):
    my_team_field_xpath = "//*[@name='myTeam']"
    enemy_team_field_xpath = "//*[@name='enemyTeam']"
    my_team_score_field_xpath = "//*[@name='myTeamScore']"
    enemy_team_score_field_xpath = "//*[@name='enemyTeamScore']"
    date_field = "//*[@name='date']"

    match_at_home_radio_xpath = '//span[text()="Match at home"]'
    match_out_home_radio_xpath = '//span[text()="Match out home"]'

    tshirt_field_xpath = "//*[@name='tshirt']"
    league_field_xpath = "//*[@name='league']"
    timePlayed_field_xpath = "//*[@name='timePlayed']"
    number_field_xpath = "//*[@name='number']"
    web_match_field_xpath = "//*[@name='webMatch']"
    general_field_xpath = "//*[@name='general']"
    rating_field_xpath = "//*[@name='timePlayed']"

    submit_button_element_xpath = '//span[text()="Submit"]'  # You can click on it
    clear_button_element_xpath = '//span[text()="Clear"]'  # You can click on it

    def type_in_my_team(self, team):
        self.field_send_keys(self.my_team_field_xpath, team)

    def click_submit_button(self):
        self.driver.find_element(By.XPATH, self.submit_button_element_xpath).click()
