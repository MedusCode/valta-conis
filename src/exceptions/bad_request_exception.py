from src.constants.http_status import HttpStatus
from src.exceptions.custom_exception import CustomException


class BadRequestException(CustomException):
    status = HttpStatus.BAD_REQUEST.value
