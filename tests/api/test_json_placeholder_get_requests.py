import pytest
import requests
from requests import Response
import json
import pprint


@pytest.mark.api
def test_get_request_posts():
    response: Response = requests.get("https://jsonplaceholder.typicode.com/posts")
    json_data = response.json()
    # pprint.pprint(json_data)
    assert response.status_code == 200
    assert response.reason == "OK"
    # print(response.headers)

@pytest.mark.api
def test_get_request_post_1():
    response: Response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200
    assert response.reason == "OK"
    json_data = response.json()
    print(json.dumps(json_data, indent=4, sort_keys=True))
    assert json_data['userId'] == 1
    assert json_data['id'] == 1
    assert json_data['title'] == "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"
    assert json_data['body'] == "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"

