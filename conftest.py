import pytest
from helpers import generate_new_courier, register_new_courier_and_return_login_password
from data import Order


@pytest.fixture(scope='function')
def courier():
    courier = generate_new_courier()
    return courier


@pytest.fixture(scope='function')
def registered_courier():
    registered_courier = register_new_courier_and_return_login_password()
    return registered_courier


@pytest.fixture(scope='function')
def order():
    order = Order()
    return order
