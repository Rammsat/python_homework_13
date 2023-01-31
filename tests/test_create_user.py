import requests
from pytest_voluptuous import S
from schemas.user import user


post_url = 'https://reqres.in/api/users'
get_url = 'https://reqres.in/api/users/'
body = {
          "name": "morpheus",
          "job": "leader"
       }


def test_status_code():
    response = requests.post(url=post_url, json=body)

    assert response.status_code == 201


def test_schema():
    response = requests.post(url=post_url, json=body)

    assert S(user) == response.json()


def test_response_should_have_param_from_request():
    response = requests.post(url=post_url, json=body)

    assert response.json().get('name') == body["name"]


def test_user_was_created():
    create_user = requests.post(url=post_url, json=body)
    user_id = create_user.json().get('id')

    response_get = requests.get(url=get_url + user_id)

    assert response_get.status_code == 200
