import json

import allure
import requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import Workflow
from Extentions.Verify_actions import Verify
from Workflow.WF_api import WF_api


class Test_json_server_api:
    url = "http://localhost:3000/"
    header = {'Content-type': 'application/json'}

    @allure.title("Getting posts list")
    @allure.description("This test is getting the posts lists and verifies the response sent back is 200")
    def test_get(self):
        result = WF_api.get_list_posts(WF_api(), self.url)
        Verify.verify_equal(self, result, 200, "Error- can't locate list of posts")

    @allure.title("Commiting a post")
    @allure.description("This test commits a post and verifies the response sent back is 201")
    def test_post(self):
        result = WF_api.commit_post(WF_api(), self.url, 'posts/', '2', '1111', 'new post', 'text 2', self.header)
        Verify.verify_equal(self, result, 201, "Error- can't add a new post")

    @allure.title("Deleting a post")
    @allure.description("This test deletes a post and verifies the response sent back is 200")
    def test_delete(self):
        result = WF_api.delete_post(WF_api(), self.url, "posts/1111", self.header)
        Verify.verify_equal(self, result, 200, "Error- deletion wasn't made")
