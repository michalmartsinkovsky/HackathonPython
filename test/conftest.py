import os
import time
import mysql.connector
import pytest
from applitools.selenium import Eyes
from selenium import webdriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from Utilities.CommonOps import CommonOps
from Utilities.Manage_pages import Manage_the_pages
from Utilities.listeners import EventListener

driver = None
#browser_type = CommonOps.get_data("browser")
eyes = None
mydb = None



@pytest.fixture(scope='class')
def init_web(request):
    browser_type = os.getenv("browser")
    if browser_type.lower() == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser_type.lower == "firefox":
        driver = webdriver.Firefox(GeckoDriverManager().install())
    elif browser_type.lower == "edge":
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    else:
        raise Exception("Wrong browser type")
   # driver = EventFiringWebDriver(driver, EventListener())          # event listener
    driver.get(CommonOps.get_data("url"))
    globals()['driver'] = driver
    eyes = Eyes()
    eyes.api_key = CommonOps.get_data("api_key")
    globals()['eyes'] = eyes
    driver.maximize_window()
    driver.implicitly_wait(10)
    Manage_the_pages.initiate_web_pages(driver)

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
    driver = EventFiringWebDriver(driver, EventListener())          # event listener
    globals()['driver'] = driver
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
    driver = EventFiringWebDriver(driver, EventListener())          # event listener
    globals()['driver'] = driver
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
    driver = EventFiringWebDriver(driver, EventListener())          # event listener
    globals()['driver'] = driver

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
