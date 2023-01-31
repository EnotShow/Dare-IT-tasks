from pages.base_page import BasePage


class AddPlayer(BasePage):

    email_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[1]/div/div/input'
    first_name_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[2]/div/div/input'
    last_name_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[3]/div/div/input'
    phone_number_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[4]/div/div/input'
    weight_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[5]/div/div/input'
    height_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[6]/div/div/input'
    birthday_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[7]/div/div/input'
    main_leg_xpath = '//*[@id="leg"]'
    club_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[9]/div/div/input'
    concurrency_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[10]/div/div/input'
    main_position_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[11]/div/div/input'
    second_position_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[12]/div/div/input'
    woewodstwo_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[12]/div/div/input'
