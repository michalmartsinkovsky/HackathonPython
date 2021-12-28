from selenium.webdriver.chrome import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import xml.etree.ElementTree as ET
from Utilities.Base import Base


class CommonOps:
    # def openWebSession(self, browser):
    #     browser = "chrome"
    #     match browser:
    #         case 'chrome':
    #             self.driver = webdriver.Chrome(ChromeDriverManager().install())
    #             self.driver.maximize_window()
    #             self.driver.get("http://localhost:3000/signin")
    #
    #         case 'firefox':
    #             self.driver = webdriver.Firefox(GeckoDriverManager().install())
    #             self.driver.maximize_window()
    #             self.driver.get("http://localhost:3000/signin")
    #
    #         case _:
    #             raise Exception("no such browser")


    def get_data(node_name):
        root = ET.parse("../config.xml").getroot()
        return root.find(".//" + node_name).text



