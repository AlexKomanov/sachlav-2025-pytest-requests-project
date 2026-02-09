import pytest
import requests
from requests import Response
import json
import pprint


@pytest.mark.api
def test_delete_request_posts():
    response: Response = requests.delete("https://jsonplaceholder.typicode.com/posts")
    json_data = response.json()
    # pprint.pprint(json_data)
    assert response.status_code == 404
    assert response.reason == "Not Found"
    assert response.ok == False

@pytest.mark.api
def test_delete_request_post_1():
    response: Response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200
    assert response.reason == "OK"
