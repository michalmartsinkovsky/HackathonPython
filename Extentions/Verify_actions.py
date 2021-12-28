import allure


class Verify:

    @staticmethod
    @allure.step("Verify equal")
    def verify_equal(actual, expected, msg):
        assert actual == expected, msg

    @allure.step("Verify true")
    @staticmethod
    def verify_true(actual):
        assert actual
