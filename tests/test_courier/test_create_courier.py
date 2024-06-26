import requests
import pytest
import allure
from data import Endpoints, Responses
from helpers import check_response, Error


class TestCreateCourier:
    @allure.title('Проверка создания курьера с обязательными параметрами')
    def test_create_courier_with_all_required_params_successfully(self, courier):
        response = requests.post(Endpoints.URL + Endpoints.COURIER_ENDPOINT, data=courier)
        assert check_response(response, Responses.COURIER_CREATE_SUCCESSFUL)

    @allure.title('Проверка создания курьера, если курьер уже создан')
    def test_create_identical_courier_unsuccessfully(self, courier):
        first_response = requests.post(Endpoints.URL + Endpoints.COURIER_ENDPOINT, data=courier)
        if first_response.status_code == 201:
            second_response = requests.post(Endpoints.URL + Endpoints.COURIER_ENDPOINT, data=courier)
            assert check_response(second_response, Responses.IDENTICAL_COURIER_CREATE_UNSUCCESSFUL)
        else:
            raise Error('Курьер не создан')

    @pytest.mark.parametrize('required_param',
                             ['login', 'password', 'firstName'],
                             ids=['курьер без логина', 'курьер без пароля', 'курьер без имени'])
    @allure.title('Проверка создания курьера без обязательных параметров')
    def test_create_courier_without_required_params_unsuccessfully(self, courier, required_param):
        del courier[required_param]
        response = requests.post(Endpoints.URL + Endpoints.COURIER_ENDPOINT, data=courier)
        assert check_response(response, Responses.COURIER_WITHOUT_REQUIRED_PARAMS_NOT_CREATED)
