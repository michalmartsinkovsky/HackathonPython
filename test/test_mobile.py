import time

import allure
import pytest
import Utilities
from Extentions.UI_actions_web import UIActions
from Extentions.Verify_actions import Verify
from Workflow.WF_mobile import Mobile_Flow


@pytest.mark.usefixtures('init_mobile')
class Test_mobile:

    # def test_number_of_icons(self):
    #
    #     expected = 18
    #     actual = Utilities.Manage_pages.mobile_home_page.get_list_of_icons_in_start_page()
    #     Verify.verify_equal(len(actual), expected,
    #                         "Error- the number of icons on start page is different than expected")

    # def test_click_tip_calculator(self):
    #     Mobile_Flow.move_to_tip_calculator()
    #     actual = UIActions.get_text(Utilities.Manage_pages.mobile_tip_page.tip_calculator_page_title())
    #     expected = "Tip Calculator"
    #     Verify.verify_equal(actual, expected, "Error- the main title of tip calculator page is different than expected")

    # @pytest.mark.dependency(depends=["test_click_tip_calculator"])
    def test_click_tip_calculator(self):
        Mobile_Flow.move_to_tip_calculator()
        time.sleep(1)
        print(Utilities.Manage_pages.mobile_tip_page.tip_calculator_page_title())
        actual = UIActions.get_text(Utilities.Manage_pages.mobile_tip_page.tip_calculator_page_title())
        expected = "Tip Calculator"
        Verify.verify_equal(actual, expected, "Error- the main title of tip calculator page is different than expected")
        Mobile_Flow.insert_bill_payment()
        time.sleep(1)
        actual = UIActions.get_text(Utilities.Manage_pages.mobile_tip_page.get_total_payment())
        time.sleep(1)
        # print("actual:",actual)
        # if actual == "1.15":
        #     expected = "1.15"
        # elif actual == "115.00":
        expected = "115.00"
        Verify.verify_equal(actual, expected, "Error- the payment + 15% tax is different than expected")

    # before method
    # def teardown_method(self):
    #     time.sleep(1)
