import pytest

from Utilities.CommonOps import CommonOps
from Workflow.WF_web import Web


@pytest.mark.usefixtures('init_web')
class Test_page_object:

    def test_01(self):
        print("1")

        Web.login_entry(self, "Katharina_Bernier", "s3cret")


