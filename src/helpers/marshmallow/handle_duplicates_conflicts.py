from src.constants.exception_message import ExceptionMessage
from src.exceptions.conflict_exception import ConflictException
from src.helpers.sqlalchemy.check_duplicates import check_entity_exists


def handle_duplicates_conflicts(
        model,
        data,
        fields_to_exception,
        exception_message,
        exception=None
):
    is_update = "initial_entity" in data
    initial_entity = data["initial_entity"] if is_update else None

    for field in fields_to_exception:
        is_duplicated = False

        if field in data and (not is_update or data[field] != getattr(initial_entity, field)):
            is_duplicated = check_entity_exists(model, field, data[field])

        if is_duplicated and not exception:
            exception = ConflictException(exception_message, details={})

        if is_duplicated and field in exception.details:
            exception.details[field].append(fields_to_exception[field])
        elif is_duplicated:
            exception.details[field] = [fields_to_exception[field]]

    if is_update:
        del data["initial_entity"]

    return {
        "data": data,
        "exception": exception
    }
