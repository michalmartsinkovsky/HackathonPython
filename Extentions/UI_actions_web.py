
class UIActions:
    @staticmethod
    def insert_text(element, word):
        element.send_keys(word)
    @staticmethod
    def click(element):
        element.click()

    @staticmethod
    def get_text(element):
        return element.text





