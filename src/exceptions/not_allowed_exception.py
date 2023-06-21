from src.constants.http_status import HttpStatus
from src.exceptions.custom_exception import CustomException


class NotAllowedException(CustomException):
    status = HttpStatus.METHOD_NOT_ALLOWED.value
