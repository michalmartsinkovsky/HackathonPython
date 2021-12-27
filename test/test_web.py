import time

import pytest

import Utilities
from Extentions.UI_actions_web import WebActions
from Extentions.Verify_actions import Verify
from Utilities.CommonOps import CommonOps

from Workflow.WF_web import Web_Flow
import Workflow


@pytest.mark.usefixtures('init_web')
class Test_page_object:

    def test_create_new_user(self):
        Web_Flow.fill_signup_form("aaaaa", "bbbbb", "cccccwwe", "yoritheking")
        Web_Flow.login_entry("cccccwwe", "yoritheking")
        time.sleep(3)

        Web_Flow.create_bank_account("leumi", "112233445", "102233445")
        actual = WebActions.get_text(Utilities.Manage_pages.home_page.get_user_name_txt())
        Verify.verify_equal(actual, "aaaaa b", "Error- the user name is incorrect")

    def test_logout(self):
        Web_Flow.click_logout()
        actual = WebActions.get_text(Utilities.Manage_pages.login_page.get_sign_page_title_txt())
        Verify.verify_equal(actual, "Sign in", "Error- the title in signin page is incorrect")

    def test_login(self):
        Web_Flow.login_entry("Katharina_Bernier", "s3cret")
        actual = WebActions.get_text(Utilities.Manage_pages.home_page.get_balance_txt())
        Verify.verify_equal(actual, "$1,681.37", "Error- the balance is incorrect")

    def test_friends_tab(self):
        Web_Flow.click_friends()
        actual = WebActions.get_text(Utilities.Manage_pages.home_page.get_friends_title_txt())
        Verify.verify_equal(actual, "Contacts", "Error- friends title is incorrect")

    def test_notification_menu(self):
        Web_Flow.click_notification()
        actual = WebActions.get_text(Utilities.Manage_pages.home_page.get_notification_title())
        Verify.verify_equal(actual, "Notifications", "Error- notification title is incorrect")
