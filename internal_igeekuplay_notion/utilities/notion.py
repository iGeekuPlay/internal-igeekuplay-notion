import requests
import json
from munch import Munch


class Notion:


    def __init__(self, secret):
        self.base_url = "https://api.notion.com/v1/"
        self.secret = secret

    def _notion_api(self, method, url, headers={},payload={}):
        url = self.base_url + url
        print(f"Calling {url}")
        headers['Authorization'] = f'Bearer {self.secret}'
        headers['Content-Type'] = 'application/json'
        headers['Notion-Version'] = '2022-02-22'

        response = requests.request(method, url, headers=headers, data=payload)
        print(response)
        return response

    def get_block_children(self, block_id):
        result = json.loads(self._notion_api("GET", f"blocks/{block_id}/children").text)

        return result

    def get_block(self, block_id):
        result = json.loads(self._notion_api("GET", f"blocks/{block_id}").text)
        return result

    def get_page(self, page_id):
        result = json.loads(self._notion_api("GET", f"pages/{page_id}").text)
        return result

    def get_user(self, user_id):
        result = json.loads(self._notion_api("GET", f"users/{user_id}").text)
        return result

    def list_users(self):
        result = json.loads(self._notion_api("GET", "users").text)
        return result

    def search_user(self, search):
        users = self.list_users()['results']
        for user in users:
            munched_user = munch(user)
            if search == munched_user.name or search == munched_user.email.split("@")[0]:
                return user

    def query_db(self, database_id, payload={}):
        result = json.loads(self._notion_api("POST", f"databases/{database_id}/query", payload=payload).text)
        return result

    def create_page(self, payload={}):
        result = json.loads(self._notion_api("POST", f"pages", payload=payload).text)
        print(result)
        return result

    @staticmethod
    def munch(d):
        return Munch.fromDict(d)
