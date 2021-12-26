from Utilities.CommonOps import CommonOps


class WebActions(CommonOps):

    def insert_text(self, word, element):
        element.send_keys(word)

    def click(self, element):
        element.click()