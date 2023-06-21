from src.helpers.marshmallow.base_dto import BaseDto
from src.helpers.marshmallow.custom_fields import CustomString
from src.helpers.marshmallow.length_validator import length_validator


class PostProductDto(BaseDto):
    product_integration_id = CustomString(required=True, validate=length_validator(1, 50))
    name = CustomString(required=True, validate=length_validator(1, 255))
    vendor_code = CustomString(required=True, validate=length_validator(1, 50))
    barcode = CustomString(required=True, validate=length_validator(1, 255))


post_product_dto = PostProductDto()
