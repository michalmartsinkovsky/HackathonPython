from Extentions.UI_actions_web import WebActions
from Pages.Web.login_page import LoginPage
from Utilities.CommonOps import CommonOps
# from test.conftest import login
from test.conftest import login


class Web(CommonOps):

    def login_entry(self, user_name, password):

        WebActions.insert_text(self.driver, user_name, LoginPage.get_user_name(self.driver))
        print("2")
        WebActions.insert_text(password, LoginPage.get_password1())
        WebActions.click(LoginPage.get_signin_btn())
