import allure
from Extentions.API_actions import API_actions


class WF_api:
    @allure.step("Commits a post")
    def commit_post(self, url, source, userId, id, title, body, header):
        return API_actions.post(API_actions(), url, source, userId, id, title, body, header)

    @allure.step("gets the list of posts")
    def get_list_posts(self, url):
        return API_actions.get(API_actions(), url)

    @allure.step("Deletes a post")
    def delete_post(self, url, source, header):
        return API_actions.delete(self, url, source, header)
