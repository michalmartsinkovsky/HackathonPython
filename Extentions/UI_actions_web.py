
class WebActions:
    @staticmethod
    def insert_text(element, word):
        element.send_keys(word)
    @staticmethod
    def click(element):
        element.click()
