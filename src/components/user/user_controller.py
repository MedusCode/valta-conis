from flask import request

from . import user_blueprint

from . import user_service
from src.components.user.data_objects.dto.post_user_dto import post_user_dto
from src.decorators.validate_body import validate_body
from .data_objects.dao.user_dao import user_only_dao, user_dao
from .data_objects.dto.get_user_dto import get_user_dto
from ...constants.http_status import HttpStatus
from ...decorators.auth_required import auth_required
from ...decorators.validate_id import validate_uuid
from ...helpers.get_initials import get_initials


@user_blueprint.post('/')
@validate_body(post_user_dto)
def post_user(request_body):
    response_body = user_only_dao.dump(user_service.create_user(request_body))

    return response_body, HttpStatus.CREATED.value


@user_blueprint.get('/me')
@auth_required(is_user_needed=True)
def get_me(current_user):
    response_body = user_dao.dump(current_user)

    return response_body, HttpStatus.OK.value


@user_blueprint.get('/')
@auth_required()
@validate_body(get_user_dto)
def get_user(request_body):
    user = user_dao.dump(user_service.get_user(**request_body))

    response_body = {
        "initials": get_initials(user['first_name'], user['second_name'], user['last_name']),
        "wallet_id": user['wallet']['id']
    }

    return response_body, HttpStatus.OK.value


@user_blueprint.get('/<string:user_id>')
@auth_required()
def get_user_by_id(user_id):
    response_body = user_only_dao.dump(user_service.get_user(user_integration_id=user_id))

    return response_body, HttpStatus.OK.value
