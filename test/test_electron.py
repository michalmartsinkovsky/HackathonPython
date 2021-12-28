import pytest
import Utilities
from Extentions.UI_actions_web import UIActions
from Extentions.Verify_actions import Verify
from Workflow.WF_electron import Web_Electron

@pytest.mark.usefixtures('init_electron')
class Test_electron:

    def test_send_ping_communication_tab(self):

        Web_Electron.ping_message()
        expected = "Synchronous message reply: pong"
        actual = UIActions.get_text(Utilities.Manage_pages.electron_home_page.get_ping_msg_txt())
        Verify.verify_equal(actual, expected, "Error- expected msg is incorrect")
