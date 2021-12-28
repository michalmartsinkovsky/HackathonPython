from Extentions.API_actions import API_actions
import test
from Utilities.CommonOps import Step


class WF_api:
    @Step ("Commits a post")
    def commit_post(self, url, source, userId, id, title, body, header):
        return API_actions.post(API_actions(), url, source, userId, id, title, body, header)

    @Step ("gets the list of posts")
    def get_list_posts(self, url):
        return API_actions.get(API_actions(), url)

    @Step ("Deletes a post")
    def delete_post(self, url, source, header):
        return API_actions.delete(self, url, source, header)
