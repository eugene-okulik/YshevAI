import allure
import requests

from YshevAI.test_api_sitd.endpoints.endpoint import Endpoint


class PostPost(Endpoint):
    @allure.step("Post request")
    def new_post(self, json_body, headers=None):
        self.body = json_body
        headers = headers if headers else self.headers
        self.response = requests.post(url=self.url, json=json_body, headers=headers)
        self.json = self.response.json()
        print(self.json)
        return self.response


