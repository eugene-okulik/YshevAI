import requests

from YshevAI.test_api_sitd.endpoints.endpoint import Endpoint


class GetPost(Endpoint):
    def req_get_by_id(self, obj_id):
        self.response = requests.get(f'{self.url}/{obj_id}')
        self.json = self.response.json()
        return self.response

    def req_get_all(self):
        self.response = requests.get(f'{self.url}')
        self.json = self.response.json()
        return self.response
