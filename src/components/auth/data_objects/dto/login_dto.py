from marshmallow import pre_load

from src.helpers.marshmallow.base_dto import BaseDto
from src.helpers.marshmallow.custom_fields import CustomString


class LoginDto(BaseDto):
    login = CustomString(required=True)
    password = CustomString(required=True)

    @pre_load
    def credentials_to_lowercase(self, credentials, **kwargs):
        credentials["login"] = credentials["login"].lower()

        return credentials


login_dto = LoginDto()
