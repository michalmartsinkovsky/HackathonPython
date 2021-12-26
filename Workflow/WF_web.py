from Extentions.UI_actions_web import WebActions
from Utilities.Manage_pages import Manage_the_pages
import Utilities



class Web_Flow:
    @staticmethod
    def login_entry(user_name, password):
        WebActions.insert_text(Utilities.Manage_pages.login.get_user_name(), user_name)
        WebActions.insert_text(Utilities.Manage_pages.login.get_password1(), password)
        WebActions.click(Utilities.Manage_pages.login.get_signin_btn())
