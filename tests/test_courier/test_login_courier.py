import requests
import allure
import pytest
from data import Endpoints, Responses
from helpers import check_response, check_response_with_dynamic_text


class TestLoginCourier:
    @allure.title('Проверка авторизации курьера с обязательными параметрами')
    def test_courier_could_login_successfully(self, registered_courier):
        response = requests.post(Endpoints.URL + Endpoints.COURIER_LOGIN_ENDPOINT, data=registered_courier)
        assert check_response_with_dynamic_text(response, Responses.COURIER_LOGIN_SUCCESSFUL)

    @pytest.mark.parametrize('required_param',
                             ['login', 'password'],
                             ids=['курьер без логина', 'курьер без пароля'])
    @allure.title('Проверка авторизации курьера без обязательных параметров')
    def test_courier_could_not_login_without_login_password(self, registered_courier, required_param):
        del registered_courier[required_param]
        response = requests.post(Endpoints.URL + Endpoints.COURIER_LOGIN_ENDPOINT, data=registered_courier)
        assert check_response(response, Responses.COURIER_LOGIN_WITHOUT_REQUIRED_PARAMS_UNSUCCESSFUL)

    @allure.title('Проверка авторизации курьера, если курьер не зарегистрирован')
    def test_unregistered_courier_could_not_login(self, courier):
        response = requests.post(Endpoints.URL + Endpoints.COURIER_LOGIN_ENDPOINT, data=courier)
        assert check_response(response, Responses.COURIER_LOGIN_WITH_WRONG_LOGIN_PASSWORD_UNSUCCESSFUL)

    @pytest.mark.parametrize('wrong_param',
                             ['login', 'password'],
                             ids=['курьер c некорректным логином', 'курьер c некорректным паролем'])
    @allure.title('Проверка авторизации курьера c некорректным логином, паролем')
    def test_courier_could_not_login_with_wrong_login_password(self, registered_courier, wrong_param):
        registered_courier[wrong_param] = 'qqqqqq'
        second_response = requests.post(Endpoints.URL + Endpoints.COURIER_LOGIN_ENDPOINT, data=registered_courier)
        assert check_response(second_response, Responses.COURIER_LOGIN_WITH_WRONG_LOGIN_PASSWORD_UNSUCCESSFUL)
