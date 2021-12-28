import allure




class UIActions:
    @staticmethod
    @allure.step("Insert text")
    def insert_text(element, word):
        element.send_keys(word)

    @staticmethod
    @allure.step("Clicks button")
    def click(element):
        element.click()

    @staticmethod
    @allure.step("Get text")
    def get_text(element):
        return element.text





