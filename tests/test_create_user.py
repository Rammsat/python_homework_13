import requests
from pytest_voluptuous import S
from schemas.user import user


post_url = 'https://reqres.in/api/users'
body = {
          "name": "morpheus",
          "job": "leader"
       }
data_for_registration = {
          "email": "eve.holt@reqres.in",
          "password": "pistol"
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


def test_login_user_who_was_registrated():
    registration = requests.post(url='https://reqres.in/api/register', json=data_for_registration)
    login = requests.get(url='https://reqres.in/api/login', json=data_for_registration)

    assert login.status_code == 200
