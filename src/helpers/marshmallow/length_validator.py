from marshmallow import validate

from src.constants.validation_message import ValidationMessage


def length_validator(min, max):
    return validate.Length(min=min, max=max, error=ValidationMessage.invalid_length(min, max))