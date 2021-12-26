import pytest

from Utilities.CommonOps import CommonOps


@pytest.mark.usefixtures('init_web')
class Test_page_object:
    def test_01(self):
        print("1")
