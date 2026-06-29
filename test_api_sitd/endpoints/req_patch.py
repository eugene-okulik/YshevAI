import allure
import requests

from YshevAI.test_api_sitd.endpoints.endpoint import Endpoint


class PatchPost(Endpoint):
    def req_patch(self, obj_id, json_body, headers=None):
        headers = headers if headers else self.headers
        self.body = json_body
        self.response = requests.patch(f'{self.url}/{obj_id}', json=json_body, headers=headers)
        self.json = self.response.json()
        return self.response
