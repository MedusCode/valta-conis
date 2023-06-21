from src.constants.http_status import HttpStatus
from src.exceptions.custom_exception import CustomException


class ForbiddenException(CustomException):
    status = HttpStatus.FORBIDDEN.value
