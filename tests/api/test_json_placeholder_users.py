import pytest
import requests
from requests import Response


@pytest.mark.api
def test_get_request_users_homework():
    response: Response = requests.get("https://jsonplaceholder.typicode.com/users")
    assert response.status_code == 200
    assert response.reason == "OK"

    users = response.json()
    assert len(users) == 10

    assert users[4]["name"] == "Chelsey Dietrich"
    assert users[7]["address"]["city"] == "Aliyaview"
    assert users[3]["id"] == 4
    assert users[3]["username"] == "Karianne"
    assert users[5]["email"] == "Karie_Dach@jasper.info"
