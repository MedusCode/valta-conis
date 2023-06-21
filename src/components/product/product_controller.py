from src.components.product import product_blueprint, product_service
from src.components.product.data_objects.dao.product_dao import product_dao, products_dao
from src.components.product.data_objects.dto.patch_product_dto import patch_product_dto
from src.components.product.data_objects.dto.post_product_dto import post_product_dto
from src.constants.http_status import HttpStatus
from src.decorators.validate_body import validate_body
from src.helpers.generate_response_list import generate_response_list


@product_blueprint.post('/')
@validate_body(post_product_dto)
def create_product(request_body):
    response_body = product_dao.dump(product_service.create_product(request_body))

    return response_body, HttpStatus.CREATED.value


@product_blueprint.get('/')
def get_products():
    products = products_dao.dump(product_service.get_all_products())

    response_body = generate_response_list(products)

    return response_body, HttpStatus.OK.value


@product_blueprint.get('/<string:product_id>')
def get_product(product_id):
    response_body = product_dao.dump(product_service.get_product(product_integration_id=product_id))

    return response_body, HttpStatus.OK.value


@product_blueprint.patch('/<string:product_id>')
@validate_body(patch_product_dto)
def update_product(product_id, request_body):
    response_body = product_dao.dump(product_service.update_product(product_id, request_body))

    return response_body, HttpStatus.OK.value


@product_blueprint.delete('/<string:product_id>')
def delete_product(product_id):
    response_body = product_dao.dump(product_service.delete_product(product_id))

    return response_body, HttpStatus.OK.value
