from src.constants.http_status import HttpStatus
from src.exceptions.custom_exception import CustomException


class ConflictException(CustomException):
    status = HttpStatus.CONFLICT.value
