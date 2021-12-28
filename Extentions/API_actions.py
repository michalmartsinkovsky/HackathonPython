import json

import allure
import requests




class API_actions:
    @allure.step("Post to API server")
    def post(self, url, source, userId, id, title, body, header):
        payload = {'userId': userId, 'id': id, 'title': title, 'body': body}
        response = requests.post(url + source, json=payload, headers=header)
        return response.status_code

    @allure.step("Get from API server")
    def get(self, url):
        search = "posts/"
        response = requests.get(url + search)
        return response.status_code

    @allure.step("Delete from API server")
    def delete(self, url, source, header):
        response = requests.delete(url + source, headers=header)
        return response.status_code
