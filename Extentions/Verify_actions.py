
class Verify:
    @staticmethod
    def verify_equal(actual, expected, msg):
        assert actual == expected, msg
    @staticmethod
    def verify_true(actual):
        assert actual
