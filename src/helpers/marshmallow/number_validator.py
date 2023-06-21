import re

from marshmallow import ValidationError

from src.constants.validation_message import ValidationMessage
from src.helpers.validators.validate_phone_number import validate_phone_number


def number_validator(number):
    if not re.match(r'^\+\d+$', number):
        raise ValidationError(ValidationMessage.PHONE_NUMBER_FORMAT.value)

    if not validate_phone_number(number):
        raise ValidationError(ValidationMessage.INVALID_PHONE_NUMBER.value)