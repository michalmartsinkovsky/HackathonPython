import time

from Extentions.UI_actions_web import WebActions
from Utilities.Manage_pages import Manage_the_pages
import Utilities



class Web_Flow:
    @staticmethod
    def login_entry(user_name, password):
        WebActions.insert_text(Utilities.Manage_pages.login_page.get_user_name_txt(), user_name)
        WebActions.insert_text(Utilities.Manage_pages.login_page.get_password_txt(), password)
        WebActions.click(Utilities.Manage_pages.login_page.get_signin_btn())


    @staticmethod
    def fill_signup_form(first_name, last_name, user_name, password):
        WebActions.click(Utilities.Manage_pages.login_page.get_create_account_btn())
        WebActions.click(Utilities.Manage_pages.login_page.get_create_account_btn())
        WebActions.insert_text(Utilities.Manage_pages.sign_up_page.get_signup_first_name_txt(), first_name)
        WebActions.insert_text(Utilities.Manage_pages.sign_up_page.get_signup_lastname_txt(), last_name)
        WebActions.insert_text(Utilities.Manage_pages.sign_up_page.get_signup_username_txt(), user_name)
        WebActions.insert_text(Utilities.Manage_pages.sign_up_page.get_signup_password_txt(), password)
        WebActions.insert_text(Utilities.Manage_pages.sign_up_page.get_signup_confirm_password_txt(), password)
        WebActions.click(Utilities.Manage_pages.sign_up_page.signup_btn())

    @staticmethod
    def create_bank_account(bank_name, routing_number, account_number):
        WebActions.click(Utilities.Manage_pages.home_page.next_btn())
        WebActions.insert_text(Utilities.Manage_pages.home_page.get_bank_name_txt(), bank_name)
        WebActions.insert_text(Utilities.Manage_pages.home_page.get_routing_number_txt(), routing_number)
        WebActions.insert_text(Utilities.Manage_pages.home_page.get_account_number_txt(), account_number)
        WebActions.click(Utilities.Manage_pages.home_page.get_save_btn())
        WebActions.click(Utilities.Manage_pages.home_page.get_done_btn())

    @staticmethod
    def click_notification():
        WebActions.click(Utilities.Manage_pages.home_page.get_notification_btn())

    @staticmethod
    def click_friends():
        WebActions.click(Utilities.Manage_pages.home_page.get_friends_tab_btn())

    @staticmethod
    def click_logout():
        WebActions.click(Utilities.Manage_pages.home_page.get_logout_btn())


