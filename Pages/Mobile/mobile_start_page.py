
from selenium.webdriver.common.by import By


class MobileStartPage:

    def __init__(self, driver):
        self.driver = driver

    def get_list_of_icons_in_start_page(self):
        return self.driver.find_elements(By.XPATH, "//*[@id='icon']")

    def tip_calculator_icon_in_start_page(self):
        print("find tip icon")
        return self.driver.find_element(By.XPATH, "//*[@text='Tip Calculator']")

