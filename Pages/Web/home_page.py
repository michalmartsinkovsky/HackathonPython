from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def next_btn(self):
        return self.driver.find_element_by_xpath("//span[text()='Next']")

    def get_bank_name_txt(self):
        return self.driver.find_element(By.XPATH, "//input[@id='bankaccount-bankName-input']")

    def get_routing_number_txt(self):
        return self.driver.find_element(By.XPATH, "//input[@id='bankaccount-routingNumber-input']")

    def get_account_number_txt(self):
        return self.driver.find_element(By.XPATH, "//input[@id='bankaccount-accountNumber-input']")

    def get_save_btn(self):
        return self.driver.find_element(By.XPATH, "//form/div[4]/div/button/span[1]")

    def get_done_btn(self):
        return self.driver.find_element(By.XPATH, "//div[3]/div/div[3]/div/div[2]")

    def get_user_name_txt(self):
        return self.driver.find_element(By.XPATH, "//h6[@data-test='sidenav-user-full-name']")

    def get_balance_txt(self):
        return self.driver.find_element(By.XPATH, "//h6[@data-test='sidenav-user-balance']")

    def get_friends_tab_btn(self):
        return self.driver.find_element(By.XPATH, "(//span[@class='MuiTab-wrapper'])[2]")

    def get_friends_title_txt(self):
        return self.driver.find_element(By.XPATH, "//div[@class='MuiListSubheader-root MuiListSubheader-sticky MuiListSubheader-gutters']")

    def get_notification_btn(self):
        return self.driver.find_element(By.XPATH, "(//div[@class='MuiListItemText-root']/span[@class='MuiTypography-root MuiListItemText-primary MuiTypography-body1 MuiTypography-displayBlock'])[4]")

    def get_notification_title(self):
        return self.driver.find_element(By.XPATH, "//main/div[2]/div/div/div/h2")

    def get_logout_btn(self):
        return self.driver.find_element(By.XPATH, "//div[5]/ul/div/div/div[2]/span")
