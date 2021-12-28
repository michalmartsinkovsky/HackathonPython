import allure
from Pages.Desktop.calculator_page import CalculatorPage
from Pages.Electron.electron_page import electronPage
from Pages.Mobile.mobile_start_page import MobileStartPage
from Pages.Mobile.tip_calculator_page import TipCalculatorPage
from Pages.Web.create_new_user_page import NewUserPage
from Pages.Web.home_page import HomePage
from Pages.Web.login_page import LoginPage

login_page = None
sign_up_page = None
home_page = None

# initiate desktop app pages
calculator_page = None

# initiate mobile app pages
mobile_home_page = None
mobile_tip_page = None

# initiate electron app pages
electron_home_page = None


class Manage_the_pages:

    @staticmethod
    @allure.step("Initiates web pages")
    def initiate_web_pages(driver):
        globals()['login_page'] = LoginPage(driver)
        globals()['sign_up_page'] = NewUserPage(driver)
        globals()['home_page'] = HomePage(driver)

    @staticmethod
    @allure.step("Initiates desktop pages")
    def initiate_desktop_page(driver):
        globals()['calculator_page'] = CalculatorPage(driver)

    @staticmethod
    @allure.step("Initiates mobile pages")
    def initiate_mobile_pages(driver):
        globals()['mobile_home_page'] = MobileStartPage(driver)
        globals()['mobile_tip_page'] = TipCalculatorPage(driver)

    @staticmethod
    @allure.step("Initiates electron pages")
    def initiate_electron_page(driver):
        globals()['electron_home_page'] = electronPage(driver)
