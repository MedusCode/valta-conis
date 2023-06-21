from functools import wraps
from flask import request
from marshmallow import ValidationError
from werkzeug.exceptions import BadRequest

from src.constants.exception_message import ExceptionMessage
from src.exceptions.bad_request_exception import BadRequestException


def validate_body(dto):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            try:
                body = request.get_json()
            except BadRequest:
                raise BadRequestException(ExceptionMessage.INVALID_BODY.value)

            if len(body) < 1:
                raise BadRequestException(ExceptionMessage.EMPTY_BODY.value)

            try:
                deserialized_body = dto.load(body)
            except ValidationError as err:
                raise BadRequestException(ExceptionMessage.INVALID_BODY.value, err.messages)

            return f(*args, **kwargs, request_body=deserialized_body)

        return decorated_function

    return decorator
