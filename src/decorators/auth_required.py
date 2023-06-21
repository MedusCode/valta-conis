import jwt
from functools import wraps
from flask import request

from src.components.user.user_model import User
from src.constants.exception_message import ExceptionMessage
from src.exceptions.unauthorized_exception import UnauthorizedException
from src.helpers.validators.validate_uuid import validate_uuid


def auth_required(is_user_needed=False):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            token = request.headers.get('authorization') or None

            if not token:
                raise UnauthorizedException(ExceptionMessage.AUTHORIZATION_HEADER_MISSED.value)

            try:
                from src.app import app
                secret = app.config.get("AUTH_SECRET")
                jwt_algorithm = app.config.get("AUTH_ALGORITHM")

                data = jwt.decode(token, secret, algorithms=jwt_algorithm)
                user_id = data['id']
            except:
                raise UnauthorizedException(ExceptionMessage.UNAUTHORIZED_USER.value)

            if not is_user_needed:
                return f(*args, **kwargs)

            user_entity = User.query.filter_by(user_integration_id=user_id).one_or_none()

            if not user_entity:
                raise UnauthorizedException(ExceptionMessage.UNAUTHORIZED_USER.value)

            return f(*args, **kwargs, current_user=user_entity)

        return decorated_function

    return decorator
