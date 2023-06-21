import jwt
from functools import wraps
from flask import request

from src import r
from src.components.user.user_model import User
from src.components.wallet.wallet_model import Wallet
from src.constants.exception_message import ExceptionMessage
from src.decorators.validate_id import validate_uuid
from src.exceptions.forbidden_exception import ForbiddenException


def transaction_token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        request_body = request.get_json()

        transaction_token = request_body["transaction_token"] if "transaction_token" in request_body else None

        if not transaction_token:
            raise ForbiddenException(ExceptionMessage.LACK_TRANSACTION_TOKEN.value)

        if r.get(transaction_token):
            raise ForbiddenException(ExceptionMessage.INVALID_TRANSACTION_TOKEN.value)

        try:
            from src.app import app
            secret = app.config.get("TRANSACTION_SECRET")
            jwt_algorithm = app.config.get("TRANSACTION_ALGORITHM")

            data = jwt.decode(transaction_token, secret, algorithms=jwt_algorithm)
            user_id = data['id']

            if not validate_uuid(user_id):
                raise Exception()
        except:
            raise ForbiddenException(ExceptionMessage.INVALID_TRANSACTION_TOKEN.value)

        user_entity = User.query.filter_by(user_integration_id=user_id).one_or_none()

        if not user_entity:
            raise ForbiddenException(ExceptionMessage.INVALID_TRANSACTION_TOKEN.value)

        return f(*args, **kwargs, destination_user_entity=user_entity, transaction_token=transaction_token)

    return decorated
