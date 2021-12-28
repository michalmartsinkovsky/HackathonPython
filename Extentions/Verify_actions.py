from Utilities.CommonOps import Step


class Verify:

    @staticmethod
    @Step("Verify equal")
    def verify_equal(actual, expected, msg):
        assert actual == expected, msg

    @Step("Verify true")
    @staticmethod
    def verify_true(actual):
        assert actual
