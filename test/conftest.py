import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from Pages.Web.login_page import LoginPage
from Utilities.CommonOps import CommonOps


driver = None
action = None
broswer = CommonOps.get_data("broswer")
login = None


@pytest.fixture(scope='class')
def init_web(request):

    # globals()['driver'] = driver
    # request.cls.driver = driver

    match broswer:
        case 'chrome':
            driver = webdriver.Chrome(ChromeDriverManager().install())
            globals()['driver'] = driver
            request.cls.driver = driver
            driver.maximize_window()
            driver.get("http://localhost:3000")
            login = LoginPage(driver)
            # globals()['login'] = login
            request.cls.login = login
            driver.implicitly_wait(10)

        case 'firefox':
            driver = webdriver.Firefox(GeckoDriverManager().install())
            driver.maximize_window()
            driver.get("http://localhost:3000/signin")

        case _:
            raise Exception("no such browser")

# yield
#     driver.quit()
#
# @pytest.fixture(scope='class')
# def init_mobile(request):
#     driver = get
#     globals()['driver'] = driver
#
#     yield
#     driver.quit()
