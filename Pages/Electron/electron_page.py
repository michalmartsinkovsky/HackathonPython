from selenium.webdriver.common.by import By


class electronPage:

    def __init__(self, driver):
        self.driver = driver

    def get_communication_menu_btn(self):
        return self.driver.find_element(By.XPATH, "//button[@id='button-ipc']")

    def get_synchronous_btn(self):
        return self.driver.find_element(By.XPATH, "//button[@id='sync-msg']")

    def get_ping_btn(self):
        return self.driver.find_element(By.XPATH, "//button[@id='sync-msg-demo-toggle']")

    def get_ping_msg_txt(self):
        return self.driver.find_element(By.XPATH, "//span[@id='sync-reply']")
