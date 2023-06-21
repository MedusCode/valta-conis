from marshmallow import validate, validates, ValidationError

from src.components.new_policy_level.new_policy_level_model import NewPolicyLevel
from src.components.sales_channel.sales_channel_model import SalesChannel
from src.constants.validation_message import ValidationMessage
from src.helpers.marshmallow.base_dto import BaseDto
from src.helpers.marshmallow.custom_fields import CustomString
from src.helpers.marshmallow.length_validator import length_validator
from src.helpers.marshmallow.number_validator import number_validator
from src.helpers.sqlalchemy.check_duplicates import check_entity_exists


class PostUserDto(BaseDto):
    user_integration_id = CustomString(required=True, validate=length_validator(1, 50))

    login = CustomString(required=True, validate=length_validator(5, 255))
    password = CustomString(required=True, validate=length_validator(7, 255))
    first_name = CustomString(required=True, validate=length_validator(1, 50))
    second_name = CustomString(validate=length_validator(1, 50))
    last_name = CustomString(required=True, validate=length_validator(1, 50))
    phone_number = CustomString(required=True, validate=length_validator(1, 20))
    email = CustomString(
        validate=[
            validate.Email(error=ValidationMessage.INVALID_EMAIL.value),
            length_validator(5, 255)
        ],
    )
    sales_channel_integration_id = CustomString(required=True, validate=length_validator(1, 50))
    new_policy_integration_id = CustomString(required=True, validate=length_validator(1, 50))

    @validates("phone_number")
    def validate_number(self, number):
        number_validator(number)


post_user_dto = PostUserDto()
