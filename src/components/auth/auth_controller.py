from flask import request, make_response

from src.components.auth import auth_blueprint, auth_service
from src.components.auth.data_objects.dto.login_dto import login_dto
from src.constants.http_status import HttpStatus
from src.decorators.validate_body import validate_body


@auth_blueprint.post('/login')
@validate_body(login_dto)
def login(request_body):
    access_token = auth_service.login(request_body)

    response_body = {
        "access_token": access_token
    }

    return response_body, HttpStatus.OK.value
