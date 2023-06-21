import uuid


def validate_uuid(value):
    try:
        uuid.UUID(str(value))
    except ValueError:
        return False

    return True
