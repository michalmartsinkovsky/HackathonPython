import allure
from Extentions.UI_actions_web import UIActions
from Utilities.Manage_pages import Manage_the_pages
import Utilities


class Desktop_Flow:
    @staticmethod
    @allure.step("Addition action")
    def sum(num1, num2, operator):
        UIActions.click(Utilities.Manage_pages.calculator_page.get_num_from_keypad_btn(num1))
        UIActions.click(Utilities.Manage_pages.calculator_page.get_operator_from_keypad_btn(operator))
        UIActions.click(Utilities.Manage_pages.calculator_page.get_num_from_keypad_btn(num2))
        UIActions.click(Utilities.Manage_pages.calculator_page.get_equal_sign_btn())

