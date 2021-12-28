
import allure
import pytest
import Utilities
from Extentions.UI_actions_web import UIActions
from Extentions.Verify_actions import Verify
from Utilities.CommonOps import CommonOps

from Utilities.Manage_database import Manage_db
from Workflow.WF_web import Web_Flow




@pytest.mark.usefixtures('init_web')
class Test_web:

    file_users = CommonOps.read_file_csv("C:/HackathonPython/Utilities/users_list.csv")

    @pytest.mark.parametrize("first_name, last_name, user_name, password", file_users)
    @allure.title("This test is creating a new user in real world web site")
    @allure.description("check if new user was created")
    def test_create_new_users_from_list(self, first_name, last_name, user_name, password):
        Web_Flow.fill_signup_form(first_name, last_name, user_name, password)

    def test_create_new_user(self):
        Web_Flow.fill_signup_form("adam", "chohen", "adam1", "yoritheking")
        Web_Flow.login_entry("adam1", "yoritheking")

        try:
            Web_Flow.create_bank_account("leumi", "112233445", "102233445")
        except:
            pass
        finally:
            actual = UIActions.get_text(Utilities.Manage_pages.home_page.get_user_name_txt())
            Verify.verify_equal(actual, "adam c", "Error- the user name is incorrect")

    @allure.title("This test is checking if logout from real world web site")
    @allure.description("check if logout was successful")
    def test_logout(self):
        Web_Flow.click_logout()
        actual = UIActions.get_text(Utilities.Manage_pages.login_page.get_sign_page_title_txt())
        Verify.verify_equal(actual, "Sign in", "Error- the title in signin page is incorrect")

    @allure.title("Login using user name and password from data base")
    @allure.description("check if new user was created")
    def test_login(self):
        result = Manage_db.get_data_from_db()
        Web_Flow.login_entry(result[0], result[1])
        actual = UIActions.get_text(Utilities.Manage_pages.home_page.get_balance_txt())
        Verify.verify_equal(actual, "$1,681.37", "Error- the balance is incorrect")

    def test_friends_tab(self):
        Web_Flow.click_friends()
        actual = UIActions.get_text(Utilities.Manage_pages.home_page.get_friends_title_txt())
        Verify.verify_equal(actual, "Contacts", "Error- friends title is incorrect")

    # Expecting to fail
    # def test_notification_menu(self):
    #     Web_Flow.graphic_check("initializing", "Comparison")
