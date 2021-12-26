from Extentions.UI_actions_web import WebActions
from Utilities.CommonOps import CommonOps


class Web(CommonOps):

    def login_entery(self):
        WebActions.insert_text("Katharina_Bernier", self.login.get_user_name())
        WebActions.insert_text("s3cret", self.login.get_password1())
        WebActions.click(self.login.get_signin_btn())
