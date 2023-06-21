from marshmallow import fields, validate

from src.components.order_product.data_objects.dto.post_order_product_dto import PostOrderProductDto
from src.constants.validation_message import ValidationMessage
from src.helpers.marshmallow.base_dto import BaseDto
from src.helpers.marshmallow.custom_fields import CustomString, CustomInteger
from src.helpers.marshmallow.length_validator import length_validator


class PostOrderDto(BaseDto):
    transaction_token = CustomString(required=True)

    order_integration_id = CustomString(required=True, validate=length_validator(1, 50))
    resource_integration_id = CustomString(required=True, validate=length_validator(1, 50))
    trading_point_integration_id = CustomString(required=True, validate=length_validator(1, 50))
    order_amount = fields.Decimal(required=True)
    address_integration_id = CustomString(required=False, validate=length_validator(1, 50))
    delivery_address = CustomString(required=False, validate=length_validator(1, 500))
    delivery_type_integration_id = CustomString(required=True, validate=length_validator(1, 50))
    payment_type_integration_id = CustomString(required=True, validate=length_validator(1, 50))
    filial_integration_id = CustomString(required=True, validate=length_validator(1, 50))
    consultant_integration_id = CustomString(required=False, validate=length_validator(1, 50))
    order_date = fields.DateTime(required=False)
    total_loyalty_points_charged = CustomInteger(
        required=False,
        validate=validate.Range(min=1, error=ValidationMessage.NOT_POSITIVE_INTEGER.value)
    )
    products = fields.List(fields.Nested(PostOrderProductDto), required=True)


post_purchase_dto = PostOrderDto()
