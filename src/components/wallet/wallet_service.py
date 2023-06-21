from src import db
from src.components.wallet.wallet_model import Wallet
from src.constants.exception_message import ExceptionMessage
from src.exceptions.bad_request_exception import BadRequestException
from src.exceptions.conflict_exception import ConflictException
from src.exceptions.not_found_exception import NotFoundException


def flush_wallet():
    wallet_entity = Wallet()

    db.session.add(wallet_entity)
    db.session.flush()

    return wallet_entity


def send_coins(sender_wallet_entity, destination_wallet_id, amount):
    if f'{sender_wallet_entity.id}' == destination_wallet_id:
        raise BadRequestException(ExceptionMessage.SELF_TRANSFER.value)

    if sender_wallet_entity.vc_balance < amount:
        raise ConflictException(ExceptionMessage.INSUFFICIENT_FUNDS.value)

    destination_wallet_entity = Wallet.query.filter_by(id=destination_wallet_id).one_or_none()

    if not destination_wallet_entity:
        raise NotFoundException(ExceptionMessage.DESTINATION_NOT_FOUND.value)

    try:
        sender_wallet_entity.vc_balance -= amount
        destination_wallet_entity.vc_balance += amount
    except Exception as exception:
        db.session.rollback()
        raise exception

    db.session.commit()
    return sender_wallet_entity


def get_transaction_token(user_entity):
    from src.app import app
    secret = app.config.get("TRANSACTION_SECRET")
    token_exp = app.config.get("TRANSACTION_TOKEN_EXP_IN_SEC")
    algorithm = app.config.get("TRANSACTION_ALGORITHM")

    transaction_token = user_entity.encode_jwt(secret, token_exp, algorithm)

    return transaction_token
