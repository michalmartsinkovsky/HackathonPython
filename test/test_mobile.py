import time
import allure
import pytest
import Utilities
from Extentions.UI_actions_web import UIActions
from Extentions.Verify_actions import Verify
from Workflow.WF_mobile import Mobile_Flow


@pytest.mark.usefixtures('init_mobile')
class Test_mobile:

    @allure.title("Mobile Financial Calculators App- counting amount of icons")
    @allure.description("This test get a list of icons on home page, than, verifies the result")
    def test_number_of_icons(self):
        expected = 18
        actual = Utilities.Manage_pages.mobile_home_page.get_list_of_icons_in_start_page()
        Verify.verify_equal(len(actual), expected,
                            "Error- the number of icons on start page is different than expected")

    @allure.title("Mobile Financial Calculators App- click on Tip Calculator icon")
    @allure.description("This test click on Tip Calculator icon, and verifies the result against the icon's title")
    def test_click_tip_calculator(self):
        Mobile_Flow.move_to_tip_calculator()
        actual = UIActions.get_text(Utilities.Manage_pages.mobile_tip_page.tip_calculator_page_title())
        expected = "Tip Calculator"
        Verify.verify_equal(actual, expected, "Error- the main title of tip calculator page is different than expected")

    @allure.title("Mobile Financial Calculators App- inserting the bill we got")
    @allure.description("This test calculates the 15% tip added to our bill and verifies the result")
    def test_insert_bill(self):
        Mobile_Flow.insert_bill_payment()
        actual = UIActions.get_text(Utilities.Manage_pages.mobile_tip_page.get_total_payment())
        expected = "115.00"
        Verify.verify_equal(actual, expected, "Error- the payment + 15% tax is different than expected")

    # before method
    def teardown_method(self):
        time.sleep(1)
