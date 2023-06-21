from marshmallow import fields

from src.constants.validation_message import ValidationMessage


class CustomString(fields.String):
    def __init__(self, *args, **kwargs):
        super(CustomString, self).__init__(*args, **kwargs)
        self.error_messages = {
            "required": ValidationMessage.REQUIRED_FIELD.value,
            "null": ValidationMessage.NULL_FIELD.value,
            "validator_failed": ValidationMessage.VALIDATOR_FAILED.value,
            "invalid": ValidationMessage.INVALID_STRING.value
        }


class CustomInteger(fields.Integer):
    def __init__(self, *args, **kwargs):
        super(CustomInteger, self).__init__(*args, **kwargs)
        self.error_messages = {
            "required": ValidationMessage.REQUIRED_FIELD.value,
            "null": ValidationMessage.NULL_FIELD.value,
            "validator_failed": ValidationMessage.VALIDATOR_FAILED.value,
            "invalid": ValidationMessage.INVALID_INTEGER.value
        }
