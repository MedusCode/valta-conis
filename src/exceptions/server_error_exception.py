from src.constants.exception_message import ExceptionMessage
from src.constants.http_status import HttpStatus
from src.exceptions.custom_exception import CustomException


class ServerErrorException(CustomException):
    status = HttpStatus.SERVER_ERROR.value

    def __init__(self, message=ExceptionMessage.SERVER_ERROR.value, *args, **kwargs):
        super(ServerErrorException, self).__init__(message, *args, **kwargs)
