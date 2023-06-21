from src.constants.exception_message import ExceptionMessage
from src.exceptions.conflict_exception import ConflictException
from src.helpers.sqlalchemy.check_duplicates import check_entity_exists


def handle_existence_conflicts(
        model,
        data,
        fields_to_exception,
        exception_message,
        exception=None
):

    for field in fields_to_exception:
        is_exists = True

        if field in data:
            is_exists = check_entity_exists(model, field, data[field])

        if not is_exists and not exception:
            exception = ConflictException(exception_message, details={})

        if not is_exists and field in exception.details:
            exception.details[field].append(fields_to_exception[field])
        elif not is_exists:
            exception.details[field] = [fields_to_exception[field]]

    return {
        "data": data,
        "exception": exception
    }
