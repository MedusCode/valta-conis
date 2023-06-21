from sqlalchemy import and_

from src import db
from src.components.loyalty_product_rule.loyalty_product_rule_model import LoyaltyProductRule
from src.components.product.data_objects.dao.product_dao import product_dao
from src.components.product.product_model import Product
from src.constants.exception_message import ExceptionMessage
from src.exceptions.not_found_exception import NotFoundException


def create_product(product):
    product_data = product_dao.load(product)

    product_entity = Product(**product_data)
    db.session.add(product_entity)
    db.session.commit()

    return product_entity


def get_all_products():
    product_entities = Product.query.all()

    return product_entities


def get_product(**kwargs):
    product_entity = Product.query.filter_by(**kwargs).one_or_none()

    if not product_entity:
        raise NotFoundException(ExceptionMessage.PRODUCT_NOT_FOUND.value)

    return product_entity


def update_product(product_id, changes):
    product_entity = get_product(product_integration_id=product_id)

    product_dao.load({
        **changes,
        "initial_entity": product_entity
    })

    for key in changes:
        setattr(product_entity, key, changes[key])

    db.session.commit()

    return product_entity


def delete_product(product_id):
    product_entity = Product.query.filter_by(product_integration_id=product_id).one_or_none()

    if product_entity:
        db.session.delete(product_entity)
        db.session.commit()
    else:
        raise NotFoundException(ExceptionMessage.PRODUCT_NOT_FOUND.value)

    return product_entity


def find_valta_product(product, user_entity):
    valta_product_entity = None
    filtered_by = None

    if "product_integration_id" in product:
        try:
            valta_product_entity = get_product(product_integration_id=product["product_integration_id"])
            valta_product_entity = Product.query.filter_by(
                product_integration_id=product["product_integration_id"]
            ).join(
                LoyaltyProductRule,
                and_(
                    LoyaltyProductRule.product_integration_id == product["product_integration_id"],
                    LoyaltyProductRule.sales_channel_integration_id == user_entity.sales_channel_integration_id,
                    LoyaltyProductRule.new_policy_integration_id == user_entity.new_policy_integration_id
                )
            ).one_or_none()
            filtered_by = "product_integration_id"
        except NotFoundException:
            pass

    if not valta_product_entity and "vendor_code" in product and "barcode" in product:
        try:
            valta_product_entity = get_product(
                vendor_code=product["vendor_code"], barcode=product["barcode"]
            ).join(
                LoyaltyProductRule,
                and_(
                    LoyaltyProductRule.product_integration_id == product["product_integration_id"],
                    LoyaltyProductRule.sales_channel_integration_id == user_entity.sales_channel_integration_id,
                    LoyaltyProductRule.new_policy_integration_id == user_entity.new_policy_integration_id
                )
            ).one_or_none()
            filtered_by = "vendor_code and barcode"
        except NotFoundException:
            pass

    if not valta_product_entity and "barcode" in product:
        try:
            valta_product_entity = get_product(
                barcode=product["barcode"]
            ).join(
                LoyaltyProductRule,
                and_(
                    LoyaltyProductRule.product_integration_id == product["product_integration_id"],
                    LoyaltyProductRule.sales_channel_integration_id == user_entity.sales_channel_integration_id,
                    LoyaltyProductRule.new_policy_integration_id == user_entity.new_policy_integration_id
                )
            ).one_or_none()
            filtered_by = "barcode"
        except NotFoundException:
            pass

    if valta_product_entity:
        print(user_entity.new_policy_integration_id)
        print(valta_product_entity.loyalty_product_rules)

    return {
        "entity": valta_product_entity,
        "filtered_by": filtered_by
    }
