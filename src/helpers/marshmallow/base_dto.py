from marshmallow import Schema

from src.constants.validation_message import ValidationMessage


class BaseDto(Schema):
    error_messages = {
        "invalid": ValidationMessage.VALIDATOR_FAILED.value,
        "unknown": ValidationMessage.UNKNOWN_FIELD.value
    }