import allure


class Endpoint:
    url = 'http://objapi.course.qa-practice.com/object'
    response = None
    headers = {'Content-Type': 'application/json'}
    body = None
    json = None

    @allure.step("Post запрос, проверка статуса кода")
    def check_response_is_correct(self):
        assert self.response.status_code == 200, f'Неуспешный запрос, код ответа: {self.response.status_code}'

    @allure.step("Проверка соответсвия по ключу name")
    def is_name_correct(self):
        sent_name = self.body["name"]
        received_name = self.json["name"]
        assert sent_name == received_name, f"They are not equal:{sent_name} is not {received_name}"

    @allure.step("Проверка соответсвия по ключу data")
    def is_data_correct(self):
        sent_body = set(self.body["data"].items())
        received_body = set(self.json["data"].items())

        assert sent_body == received_body, (f"They are not equal, difference: "
                                            f"sent json has \n{sent_body.difference(received_body)}, "
                                            f"received json has \n{received_body.difference(sent_body)}")
