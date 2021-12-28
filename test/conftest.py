import time

import mysql.connector
import pytest
from applitools.selenium import Eyes
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from Utilities.CommonOps import CommonOps
from Utilities.Manage_pages import Manage_the_pages



driver = None
browser = CommonOps.get_data("browser")
eyes = None
mydb = None



@pytest.fixture(scope='class')
def init_web(request):
    match browser:
        case 'chrome':
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.maximize_window()
            driver.get(CommonOps.get_data("url"))
            driver.implicitly_wait(10)

        case 'firefox':
            driver = webdriver.Firefox(GeckoDriverManager().install())
            driver.maximize_window()
            driver.get(CommonOps.get_data("url"))
            driver.implicitly_wait(10)
        case _:
            raise Exception("no such browser")
    Manage_the_pages.initiate_web_pages(driver)
    globals()['driver'] = driver
    eyes = Eyes()
    eyes.api_key = CommonOps.get_data("api_key")
    globals()['eyes'] = eyes

    # initiate db
    mydb = mysql.connector.connect(
        host=CommonOps.get_data("hostDB"),
        database=CommonOps.get_data("database"),
        user=CommonOps.get_data("userDB"),
        password=CommonOps.get_data("passwordDB")
    )
    globals()['mydb'] = mydb
    request.cls.mydb = mydb
    yield
    close_web_session()


@pytest.fixture(scope='class')
def init_desktop(request):
    desired_caps = {}
    desired_caps["app"] = CommonOps.get_data("app")
    desired_caps["platformName"] = CommonOps.get_data("platformName")
    desired_caps["deviceName"] = CommonOps.get_data("deviceName")
    driver = webdriver.Remote(CommonOps.get_data("desktopServer"), desired_caps)
    globals()['driver'] = driver
    request.cls.driver = driver
    globals()['driver'].implicitly_wait(5)

    Manage_the_pages.initiate_desktop_page(driver)
    yield
    close_session()


@pytest.fixture(scope='class')
def init_mobile(request):
    reportDirectory = CommonOps.get_data("reportDirectory")
    reportFormat = CommonOps.get_data("reportFormat")
    dc = {}
    testName = CommonOps.get_data("testName")
    dc['reportDirectory'] = reportDirectory
    dc['reportFormat'] = reportFormat
    dc['testName'] = testName
    dc['udid'] = 'R58R34SLXBD'
    dc['appPackage'] = 'com.financial.calculator'
    dc['appActivity'] = '.FinancialCalculators'
    dc['platformName'] = 'android'
    driver = webdriver.Remote('http://localhost:4723/wd/hub', dc)

    globals()['driver'] = driver
    request.cls.driver = driver
    globals()['driver'].implicitly_wait(5)
    Manage_the_pages.initiate_mobile_pages(driver)
    yield
    close_session()


@pytest.fixture(scope='class')
def init_electron(request):
    electron_app = CommonOps.get_data("electron_app")
    electron_driver = CommonOps.get_data("electron_driver")
    options = webdriver.ChromeOptions()
    options.binary_location = electron_app
    driver = webdriver.Chrome(chrome_options=options, executable_path=electron_driver)
    globals()['driver'] = driver
    request.cls.driver = driver
    Manage_the_pages.initiate_electron_page(driver)
    time.sleep(5)
    yield
    close_session()


def close_session():
    driver.quit()


def close_web_session():
    eyes.abort()
    mydb.close()
    driver.quit()
