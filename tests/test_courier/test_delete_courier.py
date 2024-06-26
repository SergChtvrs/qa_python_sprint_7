import requests
import allure
import pytest
from data import Endpoints, Responses
from helpers import check_response, endpoint_format


class TestDeleteCourier:
    @allure.title('Проверка успешного удаления курьера')
    def test_courier_delete_successfully(self, registered_courier):
        response = requests.post(Endpoints.URL + Endpoints.COURIER_LOGIN_ENDPOINT, data=registered_courier)
        courier_id = response.json()['id']
        courier_endpoint = endpoint_format(Endpoints.COURIER_DELETE_ENDPOINT, courier_id)
        response = requests.delete(Endpoints.URL + courier_endpoint)
        assert check_response(response, Responses.COURIER_DELETE_SUCCESSFUL)

    @pytest.mark.parametrize('id_param, response_text',
                             [('', Responses.COURIER_DELETE_WITHOUT_ID_UNSUCCESSFUL),
                              ('9999999', Responses.COURIER_DELETE_WITH_NON_EXISTENT_ID_UNSUCCESSFUL)],
                             ids=['удаление без id', 'удаление по несуществующему id'])
    @allure.title('Проверка удаления без id и удаление по несуществующему id')
    def test_courier_delete_unsuccessfully(self, id_param, response_text):
        courier_endpoint = endpoint_format(Endpoints.COURIER_DELETE_ENDPOINT, id_param)
        response = requests.delete(Endpoints.URL + courier_endpoint)
        assert check_response(response, response_text)

