import requests
import random
import string
from data import Endpoints


def generate_new_courier():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    return payload


def register_new_courier_and_return_login_password():
    new_courier = generate_new_courier()
    login_pass = {}
    response = requests.post(Endpoints.URL + Endpoints.COURIER_ENDPOINT, data=new_courier)
    if response.status_code == 201:
        login_pass['login'] = new_courier.get('login')
        login_pass['password'] = new_courier.get('password')
    return login_pass


# def register_new_courier_and_return_login_password():
#     login_pass = {}
#     payload = generate_new_courier()
#     response = requests.post(Endpoints.URL + Endpoints.COURIER_ENDPOINT, data=payload)
#     if response.status_code == 201:
#         del payload['firstName']
#         login_pass = payload
#     return login_pass


def check_response(response, expected_response):
    status_code, text = expected_response
    return response.status_code == status_code and response.text == text


def check_response_with_dynamic_text(response, expected_response):
    status_code, text = expected_response
    return response.status_code == status_code and text in response.text


def endpoint_format(endpoint, param):
    return endpoint.format(param)


class Error(Exception):
    pass
