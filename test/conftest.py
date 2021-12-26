import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from Utilities.CommonOps import CommonOps
from Utilities.Manage_pages import Manage_the_pages

driver = None
action = None
browser = CommonOps.get_data("browser")

@pytest.fixture(scope='class')
def init_web(request):

    # globals()['driver'] = driver
    # request.cls.driver = driver

    match browser:
        case 'chrome':
            driver = webdriver.Chrome(ChromeDriverManager().install())
            globals()['driver'] = driver
            request.cls.driver = driver

            driver.maximize_window()
            driver.get("http://localhost:3000")

            driver.implicitly_wait(10)
            Manage_the_pages.initiate_web_pages(driver)

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
