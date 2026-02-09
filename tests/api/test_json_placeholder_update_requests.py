import pytest
import requests
from requests import Response


@pytest.mark.api
def test_put_request_posts():
    headers_to_send = {"Content-type": "application/json; charset=UTF-8"}
    body_to_send = {
        "userId": 3,
        "id": 3,
        "title": "foo",
        "body": "bar"
    }
    response: Response = requests.put(
        url=f"https://jsonplaceholder.typicode.com/posts/{body_to_send['id']}",
        headers=headers_to_send,
        json=body_to_send
    )
    json_data = response.json()
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok == True
    assert json_data["title"] == body_to_send["title"]
    assert json_data["userId"] == body_to_send["userId"]
    assert json_data["id"] == body_to_send["id"]
    assert json_data["body"] == body_to_send["body"]


@pytest.mark.api
def test_patch_request_posts():
    headers_to_send = {"Content-type": "application/json; charset=UTF-8"}
    body_to_send = {
        "userId": 3,
        "title": "foo",

    }
    response: Response = requests.patch(
        url="https://jsonplaceholder.typicode.com/posts/3",
        headers=headers_to_send,
        json=body_to_send
    )
    json_data = response.json()
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok == True
    assert json_data["title"] == body_to_send["title"]
    assert json_data["userId"] == body_to_send["userId"]

