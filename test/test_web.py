import time

import pytest

import Utilities
from Extentions.UI_actions_web import UIActions
from Extentions.Verify_actions import Verify
from Workflow import WF_web

from Workflow.WF_web import Web_Flow


@pytest.mark.usefixtures('init_web')
class Test_web:

    def test_create_new_user(self):

        Web_Flow.fill_signup_form("adam", "chohen", "adam1", "yoritheking")
        Web_Flow.login_entry("adam1", "yoritheking")
        time.sleep(3)
        try:
            Web_Flow.create_bank_account("leumi", "112233445", "102233445")
        except:
            pass
        finally:
            actual = UIActions.get_text(Utilities.Manage_pages.home_page.get_user_name_txt())
            Verify.verify_equal(actual, "adam c", "Error- the user name is incorrect")

    def test_logout(self):
        Web_Flow.click_logout()
        actual = UIActions.get_text(Utilities.Manage_pages.login_page.get_sign_page_title_txt())
        Verify.verify_equal(actual, "Sign in", "Error- the title in signin page is incorrect")

    def test_login(self):
        Web_Flow.login_entry("Katharina_Bernier", "s3cret")
        actual = UIActions.get_text(Utilities.Manage_pages.home_page.get_balance_txt())
        Verify.verify_equal(actual, "$1,681.37", "Error- the balance is incorrect")

    def test_friends_tab(self):
        Web_Flow.click_friends()
        actual = UIActions.get_text(Utilities.Manage_pages.home_page.get_friends_title_txt())
        Verify.verify_equal(actual, "Contacts", "Error- friends title is incorrect")

    def test_notification_menu(self):
        Web_Flow.login_entry("Katharina_Bernier", "s3cret")
        Web_Flow.click_notification()
        time.sleep(2)
        Web_Flow.graphic_check ("initializing")