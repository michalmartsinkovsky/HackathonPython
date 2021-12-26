import json

import requests


class API_actions:
    def post(self, url, source, userId, id, title, body, header):
        payload = {'userId': userId, 'id': id, 'title': title, 'body': body}
        response = requests.post(url + source, json=payload, headers=header)
        return response.status_code

    def get(self, url):
        search = "posts/"
        response = requests.get(url + search)
        return response.status_code

    def delete(self, url, source, header):
        response = requests.delete(url + source, headers=header)
        return response.status_code
