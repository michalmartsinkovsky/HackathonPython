
from selenium.webdriver.common.by import By


class TipCalculatorPage:

    def __init__(self, driver):
        self.driver = driver

    def tip_calculator_page_title(self):
        return self.driver.find_element(By.XPATH, "//*[@text='Tip Calculator']")

    # def bill_input(self):
    #     return self.driver.find_element(By.XPATH, "//*[@id='billInput']")

    # def tip_input(self):
    #     return self.driver.find_element(By.XPATH, "//*[@id='tipInput']")

    def number_1_keypad(self):
        return self.driver.find_element(By.XPATH, "//*[@content-desc='1']")

    def number_0_keypad(self):
        return self.driver.find_element(By.XPATH, "//*[@content-desc='0']")

    def get_total_payment(self):
        return self.driver.find_element(By.XPATH, "//*[@id='totalCheckResult']")

