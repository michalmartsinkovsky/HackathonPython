from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from example.login_page import LoginPage
from example.main_menu import MainMenu


class Test_page_object:
    def setup_class(cls):
        global driver
        global action
        global login
        global main_menu

        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("http://localhost:3000/")
        login = LoginPage(driver)
        main_menu = MainMenu(driver)

    # def teardown_class(cls):
    #     driver.quit()

    def test_login(self):
        login.get_user_name().send_keys("Katharina_Bernier")
        login.get_password1().send_keys("s3cret")
        login.get_signin_btn()
        print(driver.current_url)


    def test_login(self):
        main_menu.get_my_account().click()

