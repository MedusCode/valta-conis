from src.constants.exception_message import ExceptionMessage
from src.exceptions.custom_exception import CustomException
from src.exceptions.not_allowed_exception import NotAllowedException
from src.exceptions.not_found_exception import NotFoundException
from src.exceptions.server_error_exception import ServerErrorException


def error_handler(exception):
    response = exception.form_response() if isinstance(exception, CustomException) else None

    if not response and exception.__class__.__name__ == 'NotFound':
        response = NotFoundException(ExceptionMessage.UNKNOWN_URL.value).form_response()

    if not response and exception.__class__.__name__ == 'MethodNotAllowed':
        response = NotAllowedException(ExceptionMessage.INVALID_METHOD.value).form_response()

    if not response:
        # TODO: logger
        print(exception.__class__.__name__)
        print(exception)
        server_error = ServerErrorException()
        response = server_error.form_response()

    return response
