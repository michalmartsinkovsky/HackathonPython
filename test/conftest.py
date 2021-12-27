import pytest
from appium.webdriver.common.touch_action import TouchAction
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from Utilities.CommonOps import CommonOps
from Utilities.Manage_pages import Manage_the_pages
from appium import webdriver

driver = None
#action = None
browser = CommonOps.get_data("browser")


@pytest.fixture(scope='class')
def init_web(request):
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
            driver.implicitly_wait(10)
        case _:
            raise Exception("no such browser")
    Manage_the_pages.initiate_web_pages(driver)
    yield
    driver.quit()


@pytest.fixture(scope='class')
def init_desktop(request):
    desired_caps = {}
    desired_caps["app"] = "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
    desired_caps["platformName"] = "Windows"
    desired_caps["deviceName"] = "WindowsPC"
    driver = webdriver.Remote("http://127.0.0.1:4723", desired_caps)
    globals()['driver'] = driver
    request.cls.driver = driver
    globals()['driver'].implicitly_wait(5)

    Manage_the_pages.initiate_desktop_page(driver)
    yield
    driver.quit()


@pytest.fixture(scope='class')
def init_mobile(request):
    reportDirectory = 'reports'
    reportFormat = 'xml'
    dc = {}
    testName = 'Untitled'
    dc['reportDirectory'] = reportDirectory
    dc['reportFormat'] = reportFormat
    dc['testName'] = testName
    dc['udid'] = 'R58R34SLXBD'
    dc['platformName'] = 'android'
    driver = webdriver.Remote('http://localhost:4723/wd/hub', dc)
    globals()['driver'] = driver
    request.cls.driver = driver
    globals()['driver'].implicitly_wait(5)
    Manage_the_pages.initiate_mobile_pages(driver)
    yield
    driver.quit()

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
