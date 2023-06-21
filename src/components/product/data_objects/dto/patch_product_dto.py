from src.helpers.marshmallow.base_dto import BaseDto
from src.helpers.marshmallow.custom_fields import CustomString
from src.helpers.marshmallow.length_validator import length_validator


class PatchProductDto(BaseDto):
    product_integration_id = CustomString(required=False, validate=length_validator(1, 50))
    name = CustomString(required=False, validate=length_validator(1, 255))
    vendor_code = CustomString(required=False, validate=length_validator(1, 50))
    barcode = CustomString(required=False, validate=length_validator(1, 255))


patch_product_dto = PatchProductDto()
