from selenium.webdriver.common.by import By


class CalculatorPage:

    def __init__(self, driver):
        self.driver = driver

    def get_num_from_keypad_btn(self, num):
        if num == '5':
            return self.driver.find_element(By.NAME, "Five")
        if num == '1':
            return self.driver.find_element(By.NAME, "One")

    def get_operator_from_keypad_btn(self, operator):
        if operator == "Plus":
            return self.driver.find_element(By.NAME, "Plus")
        if operator == "Minus":
            return self.driver.find_element(By.NAME, "Minus")
        if operator == "Multiply":
            return self.driver.find_element(By.NAME, "Multiply by")
        if operator == "Divide":
            return self.driver.find_element(By.NAME, "Divide by")

    def get_equal_sign_btn(self):
        return self.driver.find_element(By.NAME, "Equals")

    def get_display_result_txt(self):
        return self.driver.find_element(By.XPATH, "//*[@AutomationId='CalculatorResults']")
