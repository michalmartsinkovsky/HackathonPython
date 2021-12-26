import allure

from Pages.Web.login_page import LoginPage
from Utilities.Base import Base

login = None


class Manage_the_pages:

    # @allure.title("Verify Login")
    # @allure.description("check if login was succeful")
    @staticmethod
    def initiate_web_pages(driver):
        globals()['login'] = LoginPage(driver)
