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


@pytest.fixture(scope="function")
def req_new_post():
    headers = {'Content-Type': 'application/json'}
    body = {"name": "Fruits", "data": {"fruit": "apple", "color": "yellow", "count": 3}}
    response = requests.post('http://objapi.course.qa-practice.com/object', json=body, headers=headers)
    assert response.status_code == 200, f'Неуспешный запрос, код ответа: {response.status_code}'
    return response.json()["id"]


def req_delete_obj(obj_id):
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{obj_id}')
    print(response.text)
    return response


@pytest.fixture(scope="function")
def new_post_id(req_new_post):
    print("before test")
    yield req_new_post
    req_delete_obj(req_new_post)
    print("after_test")


@pytest.fixture(scope="session", autouse=True)
def inform_msg():
    print("Start testing")
    yield
    print("Testing completed")


@pytest.mark.critical
@pytest.mark.parametrize("body", [{"name": "Fruits", "data": {"fruit": "apple", "color": "yellow", "count": 3}},
                                  {"name": "Fruits", "data": {"fruit": "peach", "color": "red", "count": 7}},
                                  {"name": "Fruits", "data": {"fruit": "apple", "color": "green", "count": 2}}])
def test_req_new_post(body):
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://objapi.course.qa-practice.com/object', json=body, headers=headers)
    assert response.status_code == 200, f'Неуспешный запрос, код ответа: {response.status_code}'
    req_delete_obj(response.json()["id"])


def test_req_get(new_post_id):
    response = requests.get(f'http://objapi.course.qa-practice.com/object/{new_post_id}')
    assert response.status_code == 200, f'Неуспешный запрос, код ответа: {response.status_code}'


def test_req_put(new_post_id):
    headers = {'Content-Type': 'application/json'}
    body = {"name": "Vegetables",
            "data": {"vegetable": "carrot", "color": "orange", "count": 7}}
    response = requests.put(f'http://objapi.course.qa-practice.com/object/{new_post_id}', json=body, headers=headers)
    data = response.json()["data"]
    vegetable = data["vegetable"]
    color = data["color"]
    count = data["count"]
    assert response.json()["name"] == "Vegetables", f"Ошибка, name: {response.json()}"
    assert vegetable == "carrot", f"Ошибка, vegetable: {vegetable}"
    assert color == "orange", f"Ошибка, color: {color}"
    assert count == 7, f"Ошибка, count: {count}"


@pytest.mark.medium
def test_req_patch(new_post_id):
    headers = {'Content-Type': 'application/json'}
    body = {"name": "Fruits",
            "data": {"fruit": "apple", "color": "yellow", "count": 10}}
    response = requests.put(f'http://objapi.course.qa-practice.com/object/{new_post_id}', json=body, headers=headers)
    count = response.json()["data"]["count"]
    assert count == 10, f"Ошибка, count: {count}"


def test_req_delete(req_new_post):
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{req_new_post}')
    print(response.text)
    assert response.status_code == 200, f'Неуспешный запрос, код ответа: {response.status_code}'
    assert response.text == f"Object with id {req_new_post} successfully deleted"


def test_req_get_all():
    response = requests.get('http://objapi.course.qa-practice.com/object')
    assert response.status_code == 200, f'Неуспешный запрос, код ответа: {response.status_code}'
    print(response.json())
