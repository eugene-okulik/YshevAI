import pytest

from YshevAI.test_api_sitd.endpoints.req_post import PostPost
from YshevAI.test_api_sitd.endpoints.req_delete import DeletePost
from YshevAI.test_api_sitd.endpoints.req_get import GetPost
from YshevAI.test_api_sitd.endpoints.req_patch import PatchPost
from YshevAI.test_api_sitd.endpoints.req_put import PutPost


@pytest.fixture()
def new_obj(create_new_obj,  delete_post_endpoint):
    obj_id = create_new_obj
    print(f"obj_id: {obj_id}")
    yield obj_id
    delete_post_endpoint.req_delete(obj_id)


@pytest.fixture()
def create_new_obj(create_post_endpoint):
    obj_id = create_post_endpoint.new_post({"name": "Fruits",
                                            "data": {"fruit": "apple",
                                                     "color": "yellow",
                                                     "count": 3}}).json()["id"]
    return obj_id


@pytest.fixture()
def create_post_endpoint():
    return PostPost()


@pytest.fixture()
def delete_post_endpoint():
    return DeletePost()


@pytest.fixture()
def patch_post_endpoint():
    return PatchPost()


@pytest.fixture()
def put_post_endpoint():
    return PutPost()


@pytest.fixture()
def get_post_endpoint():
    return GetPost()
