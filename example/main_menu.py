from selenium.webdriver.common.by import By


class MainMenu:
    def __init__(self, driver):
        self.driver = driver

    def get_my_account(self):
        return self.driver.find_element(By.CLASS_NAME, "MuiListItemText")

