import allure
from Extentions.UI_actions_web import UIActions
from Utilities.Manage_pages import Manage_the_pages
import Utilities
from test import conftest


class Web_Flow:
    @staticmethod
    @allure.step("Logins")
    def login_entry(user_name, password):
        UIActions.insert_text(Utilities.Manage_pages.login_page.get_user_name_txt(), user_name)
        UIActions.insert_text(Utilities.Manage_pages.login_page.get_password_txt(), password)
        UIActions.click(Utilities.Manage_pages.login_page.get_signin_btn())

    @staticmethod
    @allure.step("filling sign-up credentials")
    def fill_signup_form(first_name, last_name, user_name, password):
        UIActions.click(Utilities.Manage_pages.login_page.get_create_account_btn())
        UIActions.click(Utilities.Manage_pages.login_page.get_create_account_btn())
        UIActions.insert_text(Utilities.Manage_pages.sign_up_page.get_signup_first_name_txt(), first_name)
        UIActions.insert_text(Utilities.Manage_pages.sign_up_page.get_signup_lastname_txt(), last_name)
        UIActions.insert_text(Utilities.Manage_pages.sign_up_page.get_signup_username_txt(), user_name)
        UIActions.insert_text(Utilities.Manage_pages.sign_up_page.get_signup_password_txt(), password)
        UIActions.insert_text(Utilities.Manage_pages.sign_up_page.get_signup_confirm_password_txt(), password)
        UIActions.click(Utilities.Manage_pages.sign_up_page.signup_btn())

    @staticmethod
    @allure.step("Creating a bank account")
    def create_bank_account(bank_name, routing_number, account_number):
        UIActions.click(Utilities.Manage_pages.home_page.next_btn())
        UIActions.insert_text(Utilities.Manage_pages.home_page.get_bank_name_txt(), bank_name)
        UIActions.insert_text(Utilities.Manage_pages.home_page.get_routing_number_txt(), routing_number)
        UIActions.insert_text(Utilities.Manage_pages.home_page.get_account_number_txt(), account_number)
        UIActions.click(Utilities.Manage_pages.home_page.get_save_btn())
        UIActions.click(Utilities.Manage_pages.home_page.get_done_btn())

    @staticmethod
    @allure.step("Navigates to notification page")
    def click_notification():
        UIActions.click(Utilities.Manage_pages.home_page.get_notification_btn())

    @staticmethod
    @allure.step("Navigates to friends tab")
    def click_friends():
        UIActions.click(Utilities.Manage_pages.home_page.get_friends_tab_btn())

    @staticmethod
    @allure.step("logging out")
    def click_logout():
        UIActions.click(Utilities.Manage_pages.home_page.get_logout_btn())

    @staticmethod
    @allure.step("Navigates to notification page")
    def graphic_check(message, message2):
        conftest.eyes.open(conftest.driver, "Realworld app", "Home title test")
        conftest.eyes.check_window(message)
        Web_Flow.click_notification()
        conftest.eyes.check_window(message2)
        conftest.eyes.close()




