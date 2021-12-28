import pytest

import test.conftest

@pytest.mark.usefixtures('init_web')
class Manage_db:
    def get_data_from_db():
        query = "SELECT * FROM users_real_world"
        my_cursor = test.conftest.mydb.cursor()
        my_cursor.execute(query)
        result = my_cursor.fetchall()

        result_str = str(result[0])
        result_str = result_str.replace(")", "").replace("(", "").replace("'", "").replace(" ", "")
        result_arr = result_str.split(",")
        return result_arr       # returning arr of user name (index 0) pass (index 1)

    # driver.find_element(By.XPATH, "//input[@name='username']").send_keys(result_arr[0])
    # driver.find_element(By.XPATH, "//input[@name='password']").send_keys(result_arr[1])
    # driver.find_element(By.XPATH, "//input[@id='submit']").click()
    # time.sleep(1)


