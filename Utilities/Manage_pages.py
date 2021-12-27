import allure

from Extentions.Verify_actions import Verify
from Pages.Web.create_new_user_page import NewUserPage
from Pages.Web.home_page import HomePage
from Pages.Web.login_page import LoginPage
from Utilities.Base import Base

login_page = None
sign_up_page = None
home_page = None
#verify = None


class Manage_the_pages:

    # @allure.title("Verify Login")
    # @allure.description("check if login was succeful")
    @staticmethod
    def initiate_web_pages(driver):
        globals()['login_page'] = LoginPage(driver)
        globals()['sign_up_page'] = NewUserPage(driver)
        globals()['home_page'] = HomePage(driver)
        #globals()['verify'] = Verify()
