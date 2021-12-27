from selenium.webdriver.common.by import By

from Extentions.UI_actions_web import UIActions


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def get_user_name_txt(self):
        return self.driver.find_element(By.XPATH, "//input[@id='username']")

    def get_password_txt(self):
        return self.driver.find_element(By.XPATH, "//input[@id='password']")

    def get_signin_btn(self):
        return self.driver.find_element(By.XPATH, "//button[@data-test='signin-submit']")

    def get_create_account_btn(self):
        return self.driver.find_element(By.XPATH, "//a[@data-test='signup']")

    def get_sign_page_title_txt(self):
        return self.driver.find_element(By.TAG_NAME, "h1")

