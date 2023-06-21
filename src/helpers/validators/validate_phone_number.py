import phonenumbers


def validate_phone_number(phone_number):
    try:
        parsed_phone_number = phonenumbers.parse(phone_number)
    except phonenumbers.NumberParseException:
        return False

    if phonenumbers.is_valid_number(parsed_phone_number):
        return True
    else:
        return False
