from . import wallet_service
from src.components.wallet import wallet_blueprint
from src.decorators.auth_required import auth_required
from src.decorators.validate_id import validate_uuid
from .data_objects.dao.wallet_dao import wallet_dao
from .data_objects.dto.get_counted_coins_dto import get_counted_coins_dto
from .data_objects.dto.post_order_dto import post_purchase_dto
from .data_objects.dto.post_transfer_dto import post_transfer_dto
from ..order import order_service
from ..order.data_objects.dao.order_dao import order_dao
from ...constants.http_status import HttpStatus
from ...decorators.transaction_token_required import transaction_token_required
from ...decorators.validate_body import validate_body


@wallet_blueprint.post('/transfer/<string:destination_wallet_id>')
@validate_uuid("destination_wallet_id")
@auth_required(is_user_needed=True)
@validate_body(post_transfer_dto)
def transfer_coins(destination_wallet_id, current_user, request_body):
    new_wallet_entity = wallet_service.send_coins(current_user.wallet, destination_wallet_id, request_body["amount"])

    response_body = wallet_dao.dump(new_wallet_entity)

    return response_body, HttpStatus.OK.value


@wallet_blueprint.get('/token')
@auth_required(is_user_needed=True)
def get_transaction_token(current_user):
    transaction_token = wallet_service.get_transaction_token(current_user)

    response_body = {
        "transaction_token": transaction_token
    }

    return response_body, HttpStatus.OK.value


@wallet_blueprint.get('/count')
@auth_required()
@validate_body(get_counted_coins_dto)
@transaction_token_required
def count_coins_for_order(request_body, destination_user_entity, transaction_token):
    order_data = request_body
    response_body = order_dao.dump(order_service.count_coins_for_order(order_data, destination_user_entity))
    #
    # return response_body, HttpStatus.OK.CREATED.value

    return "ok", 200


@wallet_blueprint.post('/order')
@auth_required()
@validate_body(post_purchase_dto)
# @transaction_token_required
def handle_order(request_body):
    order_data = request_body
    del order_data["transaction_token"]
    response_body = order_dao.dump(order_service.create_order(order_data))

    # from src.app import app
    # token_exp = app.config.get("TRANSACTION_TOKEN_EXP_IN_SEC")
    # r.set(transaction_token, 'used', ex=token_exp)

    return response_body, HttpStatus.OK.CREATED.value

