class Endpoints:
    URL = 'https://qa-scooter.praktikum-services.ru'
    COURIER_ENDPOINT = '/api/v1/courier'
    COURIER_LOGIN_ENDPOINT = '/api/v1/courier/login'
    ORDER_ENDPOINT = '/api/v1/orders'
    COURIER_DELETE_ENDPOINT = '/api/v1/courier/{}'  # id
    ORDER_ACCEPT_ENDPOINT = '/api/v1/orders/accept/{}'  # id


class Order:
    def __init__(self):
        self.firstName = "Иван"
        self.lastName = "Петров"
        self.address = "Доставочная, 112"
        self.metroStation: 55
        self.phone = "+79991112233"
        self.rentTime = 3
        self.deliveryDate = "2024-03-10"
        self.comment = "Тут комментарий"
        self.color = None


class Responses:
    COURIER_CREATE_SUCCESSFUL = [201, '{"ok":true}']
    IDENTICAL_COURIER_CREATE_UNSUCCESSFUL = [409, '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}']
    COURIER_WITHOUT_REQUIRED_PARAMS_NOT_CREATED = [400, '{"code":400,"message":"Недостаточно данных для создания учетной записи"}']
    COURIER_LOGIN_SUCCESSFUL = [200, "id"]
    COURIER_LOGIN_WITHOUT_REQUIRED_PARAMS_UNSUCCESSFUL = [400, '{"code":400,"message":"Недостаточно данных для входа"}']
    COURIER_LOGIN_AGAIN_IF_ALREADY_USE_UNSUCCESSFUL = [409, '{"code":409,"message": "Этот логин уже используется"}']
    COURIER_LOGIN_WITH_WRONG_LOGIN_PASSWORD_UNSUCCESSFUL = [404, '{"code":404,"message":"Учетная запись не найдена"}']
    ORDER_CREATE_SUCCESSFUL = [201, "track"]
    COURIER_DELETE_SUCCESSFUL = [200, '{"ok":true}']
    COURIER_DELETE_WITHOUT_ID_UNSUCCESSFUL = [400, '{code":400,"message":"Недостаточно данных для удаления курьера"}']
    COURIER_DELETE_WITH_NON_EXISTENT_ID_UNSUCCESSFUL = [404, '{"code":404,"message":"Курьера с таким id нет."}']
    ORDER_ACCEPT_SUCCESSFUL = [200, '{"ok":true}']
