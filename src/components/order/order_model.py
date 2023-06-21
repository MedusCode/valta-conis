import uuid

from sqlalchemy import UUID

from src import db
from src.components.order_product.order_product_model import OrderProduct
from src.helpers.sqlalchemy.base_model import BaseModel


class Order(BaseModel):
    __tablename__ = "initial_order"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    order_integration_id = db.Column(db.String(50), primary_key=True, unique=True)
    resource_integration_id = db.Column(db.String(50), primary_key=True)
    trading_point_integration_id = db.Column(db.String(50), nullable=False)
    order_date = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)
    order_amount = db.Column(db.Numeric(precision=4, scale=2), nullable=False)
    address_integration_id = db.Column(db.String(50), nullable=True)
    delivery_address = db.Column(db.String(500), nullable=True)
    delivery_type_integration_id = db.Column(db.String(50), nullable=False)
    payment_type_integration_id = db.Column(db.String(50), nullable=False)
    filial_integration_id = db.Column(db.String(50), nullable=False)
    consultant_integration_id = db.Column(db.String(50), nullable=True)
    total_loyalty_points_charged = db.Column(db.Integer(), nullable=True)
    products = db.relationship(OrderProduct)

    def __repr__(self):
        return f"<Order (order_integration_id={self.order_integration_id})>"
