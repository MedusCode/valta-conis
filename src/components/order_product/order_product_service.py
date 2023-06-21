from src import db
from src.components.order_product.data_objects.dao.order_product_dao import order_product_dao
from src.components.order_product.order_product_model import OrderProduct
from src.components.product import product_service


def flush_order_products(products, order_id):
    order_product_entities = []

    for product in products:
        search_result = product_service.find_valta_product(product)
        valta_product_entity = search_result["entity"]
        filtered_by = search_result["filtered_by"]

        order_product_data = order_product_dao.load({
            **product,
            "product_integration_id":
                f"{valta_product_entity.product_integration_id}" if valta_product_entity else None,
            "filtered_by": filtered_by,
            "order_integration_id": order_id
        })
        order_product_entity = OrderProduct(**order_product_data)

        db.session.add(order_product_entity)
        order_product_entities.append(order_product_entity)

    db.session.flush()

    return order_product_entities

