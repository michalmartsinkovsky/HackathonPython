import allure
from Extentions.UI_actions_web import UIActions
from Utilities.Manage_pages import Manage_the_pages
import Utilities


class Mobile_Flow:
    @staticmethod
    @allure.step("Navigates to tip calculator page")
    def move_to_tip_calculator():
        UIActions.click(Utilities.Manage_pages.mobile_home_page.tip_calculator_icon_in_start_page())

    @staticmethod
    @allure.step("Insert bill amount")
    def insert_bill_payment():
        UIActions.click(Utilities.Manage_pages.mobile_tip_page.number_1_keypad())
        UIActions.click(Utilities.Manage_pages.mobile_tip_page.number_0_keypad())
        UIActions.click(Utilities.Manage_pages.mobile_tip_page.number_0_keypad())
