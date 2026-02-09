import pytest
import requests
from requests import Response


@pytest.mark.api
def test_post_request_posts():
    headers_to_send = {"Content-type": "application/json; charset=UTF-8"}
    body_to_send = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    response: Response = requests.post(
        url="https://jsonplaceholder.typicode.com/posts",
        headers=headers_to_send,
        json=body_to_send
    )
    json_data = response.json()
    assert response.status_code == 201
    assert response.reason == "Created"
    assert response.ok == True
    assert json_data["title"] == body_to_send["title"]
    assert json_data["userId"] == body_to_send["userId"]
