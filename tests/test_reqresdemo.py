import requests
from pytest_voluptuous import S
from schemas.user import user
from utils.base_session import BaseSession


body = {
          "name": "morpheus",
          "job": "leader"
       }
data_for_registration = {
          "email": "eve.holt@reqres.in",
          "password": "pistol"
       }


def test_status_code(reqres):
    response = reqres.post(url='/users', json=body)

    assert response.status_code == 201


def test_schema(reqres):
    response = reqres.post(url='/users', json=body)

    assert S(user) == response.json()


def test_response_should_have_param_from_request(reqres):
    response = reqres.post(url='/users', json=body)

    assert response.json().get('name') == body["name"]


def test_login_user_who_was_registrated(reqres):
    registration = reqres.post(url='/register', json=data_for_registration)
    login = reqres.get(url='/login', json=data_for_registration)

    assert login.status_code == 200
