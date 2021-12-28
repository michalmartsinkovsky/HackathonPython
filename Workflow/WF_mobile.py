import time

from Extentions.UI_actions_web import UIActions
from Utilities.CommonOps import Step
from Utilities.Manage_pages import Manage_the_pages
import Utilities


class Mobile_Flow:
    @staticmethod
    @Step ("Navigates to tip calculator page")
    def move_to_tip_calculator():
        UIActions.click(Utilities.Manage_pages.mobile_home_page.tip_calculator_icon_in_start_page())

    @staticmethod
    @Step ("Insertes bill ammount")
    def insert_bill_mobile():
        UIActions.click(Utilities.Manage_pages.mobile_tip_page.number_1_keypad())
        UIActions.click(Utilities.Manage_pages.mobile_tip_page.number_0_keypad())
        UIActions.click(Utilities.Manage_pages.mobile_tip_page.number_0_keypad())
