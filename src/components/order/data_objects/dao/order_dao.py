from src import ma
from src.components.order.order_model import Order
from src.components.order_product.data_objects.dao.order_product_dao import order_product_dao


class OrderDao(ma.SQLAlchemySchema):
    class Meta:
        model = Order

    id = ma.auto_field()
    order_integration_id = ma.auto_field()
    resource_integration_id = ma.auto_field()
    trading_point_integration_id = ma.auto_field()
    order_date = ma.auto_field()
    order_amount = ma.auto_field()
    address_integration_id = ma.auto_field()
    delivery_address = ma.auto_field()
    delivery_type_integration_id = ma.auto_field()
    payment_type_integration_id = ma.auto_field()
    filial_integration_id = ma.auto_field()
    consultant_integration_id = ma.auto_field()
    total_loyalty_points_charged = ma.auto_field()
    products = ma.Nested(order_product_dao, many=True, dump_only=True)


order_dao = OrderDao()
