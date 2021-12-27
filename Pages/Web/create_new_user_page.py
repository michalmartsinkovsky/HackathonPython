from selenium.webdriver.common.by import By

from Extentions.UI_actions_web import UIActions


class NewUserPage:

    def __init__(self, driver):
        self.driver = driver

    def get_signup_first_name_txt(self):
        return self.driver.find_element(By.ID, "firstName")

    def get_signup_lastname_txt(self):
        return self.driver.find_element(By.ID, "lastName")

    def get_signup_username_txt(self):
        return self.driver.find_element(By.ID, "username")

    def get_signup_password_txt(self):
        return self.driver.find_element(By.ID, "password")

    def get_signup_confirm_password_txt(self):
        return self.driver.find_element(By.ID, "confirmPassword")

    def signup_btn(self):
        return self.driver.find_element(By.XPATH, "//span[@class='MuiButton-label'] ")

