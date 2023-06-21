from marshmallow import fields, validate

from src.constants.validation_message import ValidationMessage
from src.helpers.marshmallow.base_dto import BaseDto
from src.helpers.marshmallow.custom_fields import CustomString, CustomInteger
from src.helpers.marshmallow.length_validator import length_validator


class PostOrderProductDto(BaseDto):
    product_integration_id = CustomString(required=False, validate=length_validator(1, 50))
    name = CustomString(required=False, validate=length_validator(1, 255))
    vendor_code = CustomString(required=True, validate=length_validator(1, 50))
    barcode = CustomString(required=True, validate=length_validator(1, 255))
    quantity = fields.Decimal(required=True)
    price = fields.Decimal(required=True)
    user_price = fields.Decimal(required=True)
    automatic_discount = fields.Decimal(required=False)
    loyalty_points_charged = CustomInteger(
        required=False,
        validate=validate.Range(min=1, error=ValidationMessage.NOT_POSITIVE_INTEGER.value)
    )
    total_amount = fields.Decimal(required=True)
    is_delivered = fields.Boolean(required=False)


def lol():
    pass
