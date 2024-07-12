import requests
import allure
from data import Endpoints


class TestGetOrders:
    @allure.title('Проверка получения списка заказов')
    def test_get_orders_list_successfully(self):
        response = requests.get(Endpoints.URL + Endpoints.ORDER_ENDPOINT)
        assert len(response.json()['orders']) == 30 and response.json()['orders'][0]['track']


