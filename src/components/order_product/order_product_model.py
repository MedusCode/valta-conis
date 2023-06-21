import uuid

from sqlalchemy import UUID

from src import db
from src.helpers.sqlalchemy.base_model import BaseModel


class OrderProduct(BaseModel):
    __tablename__ = "initial_order_product"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    order_integration_id = db.Column(db.String(50), db.ForeignKey('initial_order.order_integration_id'), nullable=False)
    product_integration_id = db.Column(
        db.String(50),
        db.ForeignKey('valta_product.product_integration_id'),
        nullable=True
    )
    vendor_code = db.Column(db.String(50), nullable=False)
    barcode = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), unique=False, nullable=True)
    quantity = db.Column(db.Numeric(precision=4, scale=2), nullable=False)
    price = db.Column(db.Numeric(precision=4, scale=2), nullable=False)
    user_price = db.Column(db.Numeric(precision=4, scale=2), nullable=False)
    automatic_discount = db.Column(db.Numeric(precision=4, scale=2), nullable=True)
    loyalty_points_charged = db.Column(db.Integer, nullable=True)
    total_amount = db.Column(db.Numeric(precision=4, scale=2), nullable=False)
    is_valta_product = db.Column(db.Boolean, default=False, nullable=False)
    is_delivered = db.Column(db.Boolean, default=False, nullable=False)
    filtered_by = db.Column(db.String, nullable=True)

    def __repr__(self):
        return f"<OrderProduct (id={self.id})>"
