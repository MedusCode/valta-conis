from enum import Enum


class ExceptionMessage(Enum):
    SERVER_ERROR = 'На сервере произошла ошибка'
    UNKNOWN_URL = 'Запрошенный URL не найден на сервере'
    INVALID_METHOD = 'Запрошенный URL не поддерживает данный метод'
    INVALID_BODY = 'Неверное тело запроса'
    EMPTY_BODY = 'Тело запроса не должно быть пустым'
    FAILED_TO_CREATE = 'Не удалось создать'
    FAILED_TO_CREATE_USER = 'Не удалось создать пользователя'
    EMAIL_ALREADY_EXIST = 'Пользователь с таким email уже существует'
    LOGIN_ALREADY_EXIST = 'Пользователь с таким логином уже существует'
    PHONE_ALREADY_EXIST = 'Пользователь с таким номером телефона уже существует'
    USER_INTEGRATION_ID_ALREADY_EXISTS = 'Пользователь с таким id уже существует'
    FAILED_TO_CREATE_PRODUCT = 'Не удалось создать продукт'
    PRODUCT_INTEGRATION_ID_ALREADY_EXISTS = 'Продукт с таким id уже существует'
    BARCODE_ALREADY_EXISTS = 'Продукт с таким штрих кодом уже существует'
    VENDOR_CODE_ALREADY_EXISTS = 'Продукт с таким артикулом уже существует'
    USER_NOT_FOUND = 'Пользователь не найден'
    PRODUCT_NOT_FOUND = 'Продукт не найдет'
    INVALID_UUID = 'Неправильно указан id'
    INVALID_CREDENTIALS = 'Неверный логин или пароль'
    UNAUTHORIZED_USER = 'Пользователь не авторизован'
    AUTHORIZATION_HEADER_MISSED = 'Отсутствует заголовок авторизации'
    INSUFFICIENT_FUNDS = 'Недостаточно средств для проведений операции'
    DESTINATION_NOT_FOUND = 'Получатель не найден'
    SELF_TRANSFER = 'Id получателя и отправителя совпадают'
    LACK_TRANSACTION_TOKEN = 'Для данного действия требуется токен транзакции'
    INVALID_TRANSACTION_TOKEN = 'Время действия токена транзакции истекло или токен уже был использован'
    INVALID_NEW_POLICY_INTEGRATION_ID = "New policy с данным id не существует"
    INVALID_SALES_CHANNEL_INTEGRATION_ID = "Sales channel с данным id не существует"