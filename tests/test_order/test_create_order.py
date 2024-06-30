import requests
import pytest
import allure
import json
from data import Endpoints, Responses
from helpers import check_response_with_dynamic_text


class TestCreateOrder:
    @pytest.mark.parametrize('colors', ["'BLACK'",
                                        "'GREY'",
                                        "'BLACK', 'GREY'",
                                        ""],
                             ids=['черный', 'серый', 'черный, серый', 'без выбора цвета'])
    @allure.title('Проверка создания заказа с разными цветами самоката')
    def test_create_order_with_different_colors(self, colors, order):
        payload = order.__dict__
        payload['color'] = [colors]
        payload_string = json.dumps(payload)
        response = requests.post(Endpoints.URL + Endpoints.ORDER_ENDPOINT, data=payload_string)
        assert check_response_with_dynamic_text(response, Responses.ORDER_CREATE_SUCCESSFUL)

