
class Verify:

    def verify_equal(self, actual, expected, msg):
        assert actual == expected, msg

    def verify_true(self, actual, bool, msg):
        assert actual == bool, msg
