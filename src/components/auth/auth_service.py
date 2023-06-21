from src.components.user.user_model import User
from src.constants.exception_message import ExceptionMessage
from src.exceptions.unauthorized_exception import UnauthorizedException


def login(credentials):
    user_login = credentials["login"]
    user_password = credentials["password"]

    user_entity = User.query.filter_by(login=user_login).one_or_none()

    if not user_entity:
        raise UnauthorizedException(ExceptionMessage.INVALID_CREDENTIALS.value)

    is_matched = user_entity.check_password(user_password)

    if not is_matched:
        raise UnauthorizedException(ExceptionMessage.INVALID_CREDENTIALS.value)

    from src.app import app
    secret = app.config.get("AUTH_SECRET")
    token_exp = app.config.get("AUTH_TOKEN_EXP_IN_SEC")
    jwt_algorithm = app.config.get("AUTH_ALGORITHM")

    access_token = user_entity.encode_jwt(secret, token_exp, jwt_algorithm)

    return access_token
