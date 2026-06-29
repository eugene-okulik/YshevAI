import allure
import pytest


@allure.feature("API запросы")
@allure.story("POST запрос")
@pytest.mark.critical
@pytest.mark.parametrize("body", [{"name": "Fruits", "data": {"fruit": "apple", "color": "yellow", "count": 3}},
                                  {"name": "Fruits", "data": {"fruit": "peach", "color": "red", "count": 7}},
                                  {"name": "Fruits", "data": {"fruit": "apple", "color": "green", "count": 2}}])
def test_req_new_post(create_post_endpoint, delete_post_endpoint, body):
    create_post_endpoint.new_post(json_body=body)
    response = create_post_endpoint.json
    try:
        create_post_endpoint.check_response_is_correct()
        create_post_endpoint.is_name_correct()
        create_post_endpoint.is_data_correct()
    except AssertionError:
        raise
    finally:
        delete_post_endpoint.req_delete(response["id"])


@allure.feature("API запросы")
@allure.story("PUT запрос")
def test_req_put_post(put_post_endpoint, new_obj):
    put_post_endpoint.req_put(obj_id=new_obj, json_body={"name": "Vegetables",
                                                         "data": {"vegetable": "carrot",
                                                                  "color": "orange",
                                                                  "count": 7}})
    put_post_endpoint.check_response_is_correct()
    put_post_endpoint.is_data_correct()


@allure.feature("API запросы")
@allure.story("PATCH запрос")
@pytest.mark.medium
def test_req_patch_post(patch_post_endpoint, new_obj):
    patch_post_endpoint.req_patch(obj_id=new_obj, json_body={"data": {"count": 10}})
    patch_post_endpoint.check_response_is_correct()
    patch_post_endpoint.is_data_correct()


@allure.feature("API запросы")
@allure.story("DELETE запрос")
def test_req_delete_post(delete_post_endpoint, create_new_obj):
    delete_post_endpoint.req_delete(create_new_obj)
    delete_post_endpoint.check_response_is_correct()
    delete_post_endpoint.is_text_correct()


@pytest.mark.parametrize("post_id", [2,3,4, 5,6,7,8])
def req_delete_post(delete_post_endpoint, post_id):
    print(post_id)
    delete_post_endpoint.req_delete(post_id)


@allure.feature("API запросы")
@allure.story("GET запрос по id")
def test_req_get_post_by_id(new_obj, get_post_endpoint):
    get_post_endpoint.req_get_by_id(new_obj)
    get_post_endpoint.check_response_is_correct()


@allure.feature("API запросы")
@allure.story("GET запрос всех элементов")
def test_req_get_post_all(get_post_endpoint):
    get_post_endpoint.req_get_all()
    get_post_endpoint.check_response_is_correct()
    print(get_post_endpoint.json)