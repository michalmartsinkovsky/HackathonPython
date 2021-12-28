import csv
import xml.etree.ElementTree as ET
import allure


class CommonOps:

    @allure.step("Getting data from the configuration file")
    def get_data(node_name):
        root = ET.parse("C:\HackathonPython\config.xml").getroot()
        return root.find(".//" + node_name).text

    @allure.step("Reading external csv file")
    def read_file_csv(name_file):
        users_list_from_csv_file = []
        file1 = open(name_file, "r")
        reading = csv.reader(file1)
        for row in reading:
            users_list_from_csv_file.append(row)
        file1.close()
        return tuple(users_list_from_csv_file)

