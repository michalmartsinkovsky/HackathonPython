import json
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

    def test_get(self):
        result = WF_api.get_list_posts(WF_api(), self.url)
        Verify.verify_equal(self, result, 200, "Error- can't locate list of posts")

    def test_post(self):
        result = WF_api.commit_post(WF_api(), self.url, 'posts/', '2', '1111', 'new post', 'text 2', self.header)
        Verify.verify_equal(self, result, 201, "Error- can't add a new post")

    def test_delete(self):
        result = WF_api.delete_post(WF_api(), self.url, "posts/1111", self.header)
        Verify.verify_equal(self, result, 200, "Error- deletion wasn't made")
