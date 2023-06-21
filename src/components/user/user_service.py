from .data_objects.dao.user_dao import user_only_dao
from .user_model import User
from src import db
from ..wallet.wallet_service import flush_wallet
from ...constants.exception_message import ExceptionMessage
from ...exceptions.not_found_exception import NotFoundException
from ...exceptions.server_error_exception import ServerErrorException


def create_user(user):
    user_data = user_only_dao.load(user)

    try:
        wallet_entity = flush_wallet()
        user_entity = User(**user_data, wallet_id=wallet_entity.id)

        db.session.add(user_entity)
    except Exception as exception:
        db.rollback()
        raise exception

    db.session.commit()

    return user_entity


def get_user(**kwargs):
    user_entity = User.query.filter_by(**kwargs).one_or_none()

    if not user_entity:
        raise NotFoundException(ExceptionMessage.USER_NOT_FOUND.value)

    return user_entity
