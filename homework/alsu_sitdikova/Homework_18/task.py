"""Нужно протестировать все перечисленные в спецификации функции, а именно:

Создание объекта
Изменение объекта с помощью метода PUT
Изменение объекта с помощью метода PATCH
Удаление объекта
Выполняйте всё задание так же, как я делал на занятии, - каждый запрос в отдельной функции.
"""


import requests


def req_get_all():
    response = requests.get('http://objapi.course.qa-practice.com/object')
    assert response.status_code == 200, f'Неуспешный запрос, код ответа: {response.status_code}'
    return response.json()


def req_new_post():
    headers = {'Content-Type': 'application/json'}
    body = {"name": "Fruits",
            "data": {"fruit": "apple", "color": "yellow", "count": 3}}
    response = requests.post('http://objapi.course.qa-practice.com/object', json=body, headers=headers)
    assert response.status_code == 200, f'Неуспешный запрос, код ответа: {response.status_code}'
    return response.json()["id"]


def req_delete_obj(obj_id):
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{obj_id}')
    return response.text


def req_get():
    obj_id = req_new_post()
    response = requests.get(f'http://objapi.course.qa-practice.com/object/{obj_id}')
    assert response.status_code == 200, f'Неуспешный запрос, код ответа: {response.status_code}'
    req_delete_obj(obj_id)
    return response.json()


def req_put():
    obj_id = req_new_post()
    headers = {'Content-Type': 'application/json'}
    body = {"name": "Vegetables",
            "data": {"vegetable": "carrot", "color": "orange", "count": 7}}
    response = requests.put(f'http://objapi.course.qa-practice.com/object/{obj_id}', json=body, headers=headers)
    data = response.json()["data"]
    vegetable = data["vegetable"]
    color = data["color"]
    count = data["count"]
    assert response.json()["name"] == "Vegetables", f"Ошибка, name: {response.json()}"
    assert vegetable == "carrot", f"Ошибка, vegetable: {vegetable}"
    assert color == "orange", f"Ошибка, color: {color}"
    assert count == 7, f"Ошибка, count: {count}"
    req_delete_obj(obj_id)


def req_patch():
    obj_id = req_new_post()
    headers = {'Content-Type': 'application/json'}
    body = {"name": "Fruits",
            "data": {"fruit": "apple", "color": "yellow", "count": 10}}
    response = requests.put(f'http://objapi.course.qa-practice.com/object/{obj_id}', json=body, headers=headers)
    count = response.json()["data"]["count"]
    assert count == 10, f"Ошибка, count: {count}"
    req_delete_obj(obj_id)


def req_delete():
    obj_id = req_new_post()
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{obj_id}')
    assert response.text == f"Object with id {obj_id} successfully deleted"
    assert response.status_code == 200, f'Неуспешный запрос, код ответа: {response.status_code}'


req_get()
req_put()
req_patch()
req_delete()

print(req_get_all())
