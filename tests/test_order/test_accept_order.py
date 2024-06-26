import requests
import allure
from data import Endpoints, Responses
from helpers import endpoint_format, check_response


class TestAcceptOrder:
    @allure.title('Проверка успешного принятия заказа курьером')
    def test_accept_order_successful(self, registered_courier):
        response = requests.post(Endpoints.URL + Endpoints.COURIER_LOGIN_ENDPOINT, data=registered_courier)
        courier_id = response.json()['id']
        response = requests.get(Endpoints.URL + Endpoints.ORDER_ENDPOINT)
        order_id = response.json()['orders'][-1]['id']
        accept_endpoint = endpoint_format(Endpoints.ORDER_ACCEPT_ENDPOINT, order_id)
        params = {'courierId': courier_id}
        response = requests.put(Endpoints.URL + accept_endpoint, params=params)
        assert check_response(response, Responses.ORDER_ACCEPT_SUCCESSFUL)

