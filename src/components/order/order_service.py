from src import db
from src.components.order.data_objects.dao.order_dao import order_dao
from src.components.order.order_model import Order
from src.components.order_product import order_product_service
from src.components.order_product.order_product_model import OrderProduct
from src.components.product import product_service


def count_coins_for_order(order, user_entity):
    products = order["products"]

    for product in products:
        search_result = product_service.find_valta_product(product, user_entity)

        if search_result["entity"]:
            print(search_result["entity"].loyalty_product_rules)


def create_order(order):
    products = order["products"]

    del order["products"]
    order_data = order_dao.load(order)

    order_entity = Order(**order_data)

    try:
        db.session.add(order_entity)
        db.session.flush()
        order_product_service.flush_order_products(products, f'{order_entity.order_integration_id}')
    except Exception as exception:
        db.session.rollback()
        raise exception

    db.session.commit()

    final_order_entity = Order.query.filter_by(
        order_integration_id=order_entity.order_integration_id
    ).join(OrderProduct, OrderProduct.order_integration_id == Order.order_integration_id).one_or_none()

    return final_order_entity
