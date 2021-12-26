from Extentions.API_actions import API_actions
import test


class WF_api:
    def commit_post(self, url, source, userId, id, title, body, header):
        return API_actions.post(API_actions(), url, source, userId, id, title, body, header)

    def get_list_posts(self, url):
        return API_actions.get(API_actions(), url)

    def delete_post(self, url, source, header):
        return API_actions.delete(self, url, source, header)
