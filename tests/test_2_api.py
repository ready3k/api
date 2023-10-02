from api.questions_api import api
from http import HTTPStatus
from utils.assertions import Assert


def test_list_users():
    assert api.list_users().status_code == HTTPStatus.OK
#    Assert.validate_schema(res.json())


def test_single_user():
    res = api.single_user()
    res_body = res.json()

    assert res.status_code == HTTPStatus.OK
#   Assert.validate_schema(res_body)
    assert res_body["data"]["first_name"] == "Janet"
    example = {
        "data": {
            "id": 2,
            "email": "janet.weaver@reqres.in",
            "first_name": "Janet",
            "last_name": "Weaver",
            "avatar": "https://reqres.in/img/faces/2-image.jpg"
        },
        "support": {
            "url": "https://reqres.in/#support-heading",
            "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
        }
    }
    assert example == res_body


def test_single_user_not_found():
    assert api.single_user_not_found().status_code == HTTPStatus.NOT_FOUND
#    Assert.validate_schema(res.json())


def test_create():
    name = "Rodion"
    job = "student"
    res = api.create(name, job)
    assert res.status_code == HTTPStatus.CREATED
#    Assert.validate_schema(res_body)
    assert res.json()["name"] == name
    assert res.json()["job"] == job
    assert api.delete_user(res.json()['id']).status_code == HTTPStatus.NO_CONTENT
