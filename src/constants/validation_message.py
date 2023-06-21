from enum import Enum


class ValidationMessage(Enum):
    REQUIRED_FIELD  = "Отсутствуют данные для обязательного поля"
    NULL_FIELD = "Поле не может быть пустым"
    INVALID_STRING = "Поле должно быть строкой (String)"
    INVALID_INTEGER = "Поле должно быть целым числом (Integer)"
    VALIDATOR_FAILED = "Неверное значение"
    PHONE_NUMBER_FORMAT = "Формат номера телефона должен соответствовать '+XXXXXXXXXX'"
    INVALID_PHONE_NUMBER = "Невозможный номер телефона"
    INVALID_EMAIL = "Невозможный email"
    UNKNOWN_FIELD = "Неизвестное поле"
    NOT_POSITIVE_INTEGER = "Число должно быть больше нуля"

    @staticmethod
    def invalid_length(from_number, to_number):
        return f"Длина строки должно быть между {from_number} и {to_number}"