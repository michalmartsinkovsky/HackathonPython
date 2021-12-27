
class WebActions:
    @staticmethod
    def insert_text(element, word):
        element.send_keys(word)
    @staticmethod
    def click(element):
        element.click()

    @staticmethod
    def get_text(element):
        print(element.text)
        return element.text


