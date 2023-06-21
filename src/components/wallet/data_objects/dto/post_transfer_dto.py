from marshmallow import validate

from src.constants.validation_message import ValidationMessage
from src.helpers.marshmallow.base_dto import BaseDto
from src.helpers.marshmallow.custom_fields import CustomInteger


class PostTransferDto(BaseDto):
    amount = CustomInteger(
        required=True,
        validate=validate.Range(min=1, error=ValidationMessage.NOT_POSITIVE_INTEGER.value)
    )


post_transfer_dto = PostTransferDto()


