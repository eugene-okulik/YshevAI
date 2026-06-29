import allure
import requests

from YshevAI.test_api_sitd.endpoints.endpoint import Endpoint


class DeletePost(Endpoint):
    def __init__(self):
        self.obj_id = None
        self.text = None

    def req_delete(self, obj_id):
        self.obj_id = obj_id
        self.response = requests.delete(f'{self.url}/{obj_id}')
        self.text = self.response.text
        print('text: ', self.text)

    @allure.step("Проверка соответсвия id удаленного элемента")
    def is_text_correct(self):
        assert self.response.text == f"Object with id {self.obj_id} successfully deleted", \
                                     f"Text is not expected: {self.response.text}"
