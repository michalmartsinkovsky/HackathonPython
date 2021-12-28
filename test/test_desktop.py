import time

import allure
import pytest
import Utilities
from Extentions.UI_actions_web import UIActions
from Extentions.Verify_actions import Verify
from Workflow.WF_desktop import Desktop_Flow



@pytest.mark.usefixtures('init_desktop')
class Test_calculator:

    @allure.title("Addition")
    @allure.description("This test makes an addition calculation and verifies the result")
    def test_operation_on_calc_app(self):
        Desktop_Flow.sum("1", "5", "Plus")
        expected = "Display is 6"
        actual = UIActions.get_text(Utilities.Manage_pages.calculator_page.get_display_result_txt())
        print(actual)
        Verify.verify_equal(actual, expected, "Error- the sum is incorrect")
