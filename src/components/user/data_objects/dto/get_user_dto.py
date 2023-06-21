from marshmallow import validate, validates

from src.constants.validation_message import ValidationMessage
from src.helpers.marshmallow.base_dto import BaseDto
from src.helpers.marshmallow.custom_fields import CustomString
from src.helpers.marshmallow.length_validator import length_validator
from src.helpers.marshmallow.number_validator import number_validator


class GetUserDto(BaseDto):
    login = CustomString(validate=length_validator(5, 255))
    phone_number = CustomString(validate=length_validator(1, 20))
    email = CustomString(
        validate=[
            validate.Email(error=ValidationMessage.INVALID_EMAIL.value),
            length_validator(5, 255)
        ],
    )

    @validates("phone_number")
    def validate_number(self, number):
        number_validator(number)


get_user_dto = GetUserDto()
