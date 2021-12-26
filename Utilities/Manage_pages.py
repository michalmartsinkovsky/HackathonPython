import allure

from Pages.Web.login_page import LoginPage
from Utilities.Base import Base


class Manage_pages(Base):

    # @allure.title("Verify Login")
    # @allure.description("check if login was succeful")

    @allure.step("check home page title")
    def initiate_web_pages(self):
        login = LoginPage(self.driver)

