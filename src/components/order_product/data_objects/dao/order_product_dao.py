from src import ma
from src.components.order_product.order_product_model import OrderProduct


class OrderProductDao(ma.SQLAlchemySchema):
    class Meta:
        model = OrderProduct

    order_integration_id = ma.auto_field()
    product_integration_id = ma.auto_field()
    vendor_code = ma.auto_field()
    barcode = ma.auto_field()
    name = ma.auto_field()
    quantity = ma.auto_field()
    price = ma.auto_field()
    user_price = ma.auto_field()
    automatic_discount = ma.auto_field()
    loyalty_points_charged = ma.auto_field()
    total_amount = ma.auto_field()
    is_valta_product = ma.auto_field()
    is_delivered = ma.auto_field()
    filtered_by = ma.auto_field()


order_product_dao = OrderProductDao()
