"""Задание
Оформите тесты из задания 19 как тесты, которые можно запустить с помощью Pytest.
Тест на создание объекта оформите так, чтобы он тестировал создание трёх разных объектов с помощью parametrize
Сделайте так, чтобы перед запуском всех тестов распечатывалось "Start testing",
а по завершении всех тестов - "Testing completed"
Сделайте так, чтобы перед каждым тестом распечатывалось "before test", а после каждого теста - "after test"
Пометьте 1 тест как "critical", а один тест как "medium". Сделайте так, чтобы при выполнении тестов в терминале
не было ошибок и ворнингов.
Тесты на изменение, получение по id и удаление объекта сделайте независимыми. Т.е. сделайте так,
чтобы перед запуском каждого из этих тестов запускалось выполнение предусловия - создание объекта для этого теста,
в после теста, пусть созданный объект удаляется.
"""

import requests
import pytest
import allure


@pytest.fixture(scope="function")
def new_obj_id():
    headers = {'Content-Type': 'application/json'}
    body = {"name": "Fruits", "data": {"fruit": "apple", "color": "yellow", "count": 3}}
    response = requests.post('http://objapi.course.qa-practice.com/object', json=body, headers=headers)
    assert response.status_code == 200, f'Неуспешный запрос, код ответа: {response.status_code}'
    return response.json()["id"]


def req_delete_obj(obj_id):
    with allure.step(f"Удаление объекта с id: {obj_id}"):
        response = requests.delete(f'http://objapi.course.qa-practice.com/object/{obj_id}')
        print(response.text)
        return response


@pytest.fixture(scope="function")
def new_post_id(new_obj_id):
    print("before test")
    yield new_obj_id
    req_delete_obj(new_obj_id)
    print("after_test")


@pytest.fixture(scope="session", autouse=True)
def inform_msg():
    print("Start testing")
    yield
    print("Testing completed")


@allure.feature("API запросы")
@allure.story("POST запрос")
@pytest.mark.critical
@pytest.mark.parametrize("body", [{"name": "Fruits", "data": {"fruit": "apple", "color": "yellow", "count": 3}},
                                  {"name": "Fruits", "data": {"fruit": "peach", "color": "red", "count": 7}},
                                  {"name": "Fruits", "data": {"fruit": "apple", "color": "green", "count": 2}}])
def test_req_new_post(body):
    headers = {'Content-Type': 'application/json'}
    with allure.step("Post запрос создание нового объекта"):
        response = requests.post('http://objapi.course.qa-practice.com/object', json=body, headers=headers)
    with allure.step("Post запрос, проверка статуса кода"):
        assert response.status_code == 200, f'Неуспешный запрос, код ответа: {response.status_code}'
    req_delete_obj(response.json()["id"])


@allure.feature("API запросы")
@allure.story("GET запрос по id")
def test_req_get(new_post_id):
    with allure.step("GET запрос объекта по id"):
        response = requests.get(f'http://objapi.course.qa-practice.com/object/{new_post_id}')
    with allure.step("Post запрос, проверка статуса кода"):
        assert response.status_code == 200, f'Неуспешный запрос, код ответа: {response.status_code}'


@allure.feature("API запросы")
@allure.story("PUT запрос")
def test_req_put(new_post_id):
    headers = {'Content-Type': 'application/json'}
    body = {"name": "Vegetables",
            "data": {"vegetable": "carrot", "color": "orange", "count": 7}}
    with allure.step("PUT запрос по id"):
        response = requests.put(f'http://objapi.course.qa-practice.com/object/{new_post_id}',
                                json=body,
                                headers=headers)
        data = response.json()["data"]
        vegetable = data["vegetable"]
        color = data["color"]
        count = data["count"]
    with allure.step("PUT запрос проверка соответствия значения name 'Vegetables'"):
        assert response.json()["name"] == "Vegetables", f"Ошибка, name: {response.json()}"
    with allure.step("PUT запрос проверка соответствия значения vegetable 'carrot'"):
        assert vegetable == "carrot", f"Ошибка, vegetable: {vegetable}"
    with allure.step("PUT запрос проверка соответствия значения color 'orange'"):
        assert color == "orange", f"Ошибка, color: {color}"
    with allure.step("PUT запрос проверка соответствия значения count '7'"):
        assert count == 7, f"Ошибка, count: {count}"


@allure.feature("API запросы")
@allure.story("PATCH запрос")
@pytest.mark.medium
def test_req_patch(new_post_id):
    headers = {'Content-Type': 'application/json'}
    body = {"data": {"count": 10}}
    with allure.step("PATCH запрос по id"):
        response = requests.patch(f'http://objapi.course.qa-practice.com/object/{new_post_id}',
                                  json=body,
                                  headers=headers)
    count = response.json()["data"]["count"]
    with allure.step("PATCH запрос проверка соответствия значения count '10'"):
        assert count == 10, f"Ошибка, count: {count}"


@allure.feature("API запросы")
@allure.story("DELETE запрос")
def test_req_delete(new_obj_id):
    with allure.step("DELETE запрос по id"):
        response = requests.delete(f'http://objapi.course.qa-practice.com/object/{new_obj_id}')
    print(response.text)
    with allure.step("DELETE запрос по id, проверка статуса кода"):
        assert response.status_code == 200, f'Неуспешный запрос, код ответа: {response.status_code}'
    with allure.step("DELETE запрос по id, тескт ответа после удаления объекта"):
        assert response.text == f"Object with id {new_obj_id} successfully deleted"


@allure.feature("API запросы")
@allure.story("GET запрос всех элементов")
def test_req_get_all():
    with allure.step("GET запрос всех элементов"):
        response = requests.get('http://objapi.course.qa-practice.com/object')
    with allure.step("GET запрос, проверка статуса кода"):
        assert response.status_code == 200, f'Неуспешный запрос, код ответа: {response.status_code}'
        print(response.json())
