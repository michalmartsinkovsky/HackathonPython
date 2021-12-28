import time

from Extentions.UI_actions_web import UIActions
from Utilities.Manage_pages import Manage_the_pages
import Utilities


class Web_Electron:
    @staticmethod
    def ping_message():
        UIActions.click(Utilities.Manage_pages.electron_home_page.get_communication_menu_btn())
        time.sleep(1)
        if not Utilities.Manage_pages.electron_home_page.get_synchronous_btn().is_displayed():
            UIActions.click(Utilities.Manage_pages.electron_home_page.get_ping_btn())
        time.sleep(1)
        UIActions.click(Utilities.Manage_pages.electron_home_page.get_synchronous_btn())
        time.sleep(1)
