from src import ma
from marshmallow import pre_load

from src.components.new_policy_level.new_policy_level_model import NewPolicyLevel
from src.components.sales_channel.sales_channel_model import SalesChannel
from src.components.user.user_model import User
from src.components.wallet.data_objects.dao.wallet_dao import wallet_dao
from src.constants.exception_message import ExceptionMessage
from src.helpers.marshmallow.handle_duplicates_conflicts import handle_duplicates_conflicts
from src.helpers.marshmallow.handle_existence_conflicts import handle_existence_conflicts


class UserDao(ma.SQLAlchemySchema):
    class Meta:
        model = User

    user_integration_id = ma.auto_field()
    email = ma.auto_field()
    login = ma.auto_field()
    first_name = ma.auto_field()
    second_name = ma.auto_field()
    last_name = ma.auto_field()
    phone_number = ma.auto_field()
    password = ma.String(key="password_hash")
    sales_channel_integration_id = ma.auto_field()
    new_policy_integration_id = ma.auto_field()
    wallet = ma.Nested(wallet_dao)

    @pre_load
    def pre_load_validation(self, user, **_):
        results = handle_existence_conflicts(
            SalesChannel,
            user,
            {
                "sales_channel_integration_id": ExceptionMessage.INVALID_SALES_CHANNEL_INTEGRATION_ID.value,
            },
            ExceptionMessage.FAILED_TO_CREATE_USER.value
        )

        results = handle_existence_conflicts(
            NewPolicyLevel,
            user,
            {
                "new_policy_integration_id": ExceptionMessage.INVALID_NEW_POLICY_INTEGRATION_ID.value,
            },
            ExceptionMessage.FAILED_TO_CREATE_USER.value,
            exception=results["exception"]
        )

        results = handle_duplicates_conflicts(
            self.Meta.model,
            user,
            {
                "user_integration_id": ExceptionMessage.USER_INTEGRATION_ID_ALREADY_EXISTS.value,
                "login": ExceptionMessage.LOGIN_ALREADY_EXIST.value,
                "phone_number": ExceptionMessage.PHONE_ALREADY_EXIST.value,
                "email": ExceptionMessage.EMAIL_ALREADY_EXIST.value
            },
            ExceptionMessage.FAILED_TO_CREATE_USER.value,
            exception=results["exception"]
        )

        if results["exception"]:
            raise results["exception"]

        return results["data"]

    @pre_load
    def capitalize_name(self, user, **_):
        first_name = user["first_name"]
        second_name = user["second_name"] if "second_name" in user else None
        last_name = user["last_name"]

        user["first_name"] = first_name.capitalize() if isinstance(first_name, str) else first_name
        user["second_name"] = second_name.capitalize() if isinstance(second_name, str) else second_name
        user["last_name"] = last_name.capitalize() if isinstance(last_name, str) else last_name

        return user

    @pre_load
    def credentials_to_lowercase(self, user, **_):
        user["login"] = user["login"].lower()
        user["email"] = user["email"].lower() if "email" in user else None

        return user


user_only_dao = UserDao(exclude=["wallet"])
user_dao = UserDao()
