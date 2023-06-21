from functools import wraps

from src.constants.exception_message import ExceptionMessage
from src.exceptions.bad_request_exception import BadRequestException
from src.helpers.validators.validate_uuid import validate_uuid as validate


def validate_uuid(key):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            uuid = kwargs[key]

            if not validate(uuid):
                raise BadRequestException(ExceptionMessage.INVALID_UUID.value)

            return f(*args, **kwargs)

        return decorated_function

    return decorator
