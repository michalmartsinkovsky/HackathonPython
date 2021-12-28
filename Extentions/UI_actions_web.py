from Utilities.CommonOps import Step


class UIActions:
    @staticmethod
    @Step("Insert text")
    def insert_text(element, word):
        element.send_keys(word)

    @staticmethod
    @Step("Clicks button")
    def click(element):
        element.click()

    @staticmethod
    @Step("Get text")
    def get_text(element):
        return element.text





