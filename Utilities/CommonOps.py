import csv
import xml.etree.ElementTree as ET


class CommonOps:

    def get_data(node_name):
        root = ET.parse("../config.xml").getroot()
        return root.find(".//" + node_name).text

    def read_file_csv(name_file):

        users_list_from_csv_file = []
        file1 = open(name_file, "r")
        reading = csv.reader(file1)
        for row in reading:
            users_list_from_csv_file.append(row)
        file1.close()
        return tuple(users_list_from_csv_file)


