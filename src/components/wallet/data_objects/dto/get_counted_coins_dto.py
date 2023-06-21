from marshmallow import fields

from src.components.order_product.data_objects.dto.post_order_product_dto import PostOrderProductDto
from src.helpers.marshmallow.base_dto import BaseDto
from src.helpers.marshmallow.custom_fields import CustomString
from src.helpers.marshmallow.length_validator import length_validator


class GetCountedCoinsDto(BaseDto):
    transaction_token = CustomString(required=True)

    order_integration_id = CustomString(required=False, validate=length_validator(1, 50))
    resource_integration_id = CustomString(required=True, validate=length_validator(1, 50))
    trading_point_integration_id = CustomString(required=True, validate=length_validator(1, 50))
    order_amount = fields.Decimal(required=False)
    address_integration_id = CustomString(required=False, validate=length_validator(1, 50))
    delivery_address = CustomString(required=False, validate=length_validator(1, 500))
    delivery_type_integration_id = CustomString(required=True, validate=length_validator(1, 50))
    payment_type_integration_id = CustomString(required=False, validate=length_validator(1, 50))
    filial_integration_id = CustomString(required=False, validate=length_validator(1, 50))
    consultant_integration_id = CustomString(required=False, validate=length_validator(1, 50))
    products = fields.List(fields.Nested(PostOrderProductDto), required=True)


get_counted_coins_dto = GetCountedCoinsDto()
