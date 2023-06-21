import uuid

from sqlalchemy import UUID

from src import db
from src.helpers.sqlalchemy.base_model import BaseModel


class LoyaltyProductRule(BaseModel):
    __tablename__ = "loyalty_product_rule"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    loyalty_product_rule_id = db.Column(db.String(50), primary_key=True, unique=True)
    product_integration_id = db.Column(
        db.String(50),
        db.ForeignKey('valta_product.product_integration_id'),
        nullable=False
    )
    sales_channel_integration_id = db.Column(
        db.String(50),
        db.ForeignKey('sales_channel.sales_channel_integration_id'),
        nullable=True
    )
    new_policy_integration_id = db.Column(
        db.String(50),
        db.ForeignKey('new_policy_level.new_policy_integration_id'),
        nullable=True
    )
    cashback_percent = db.Column(db.Integer(), nullable=False)
    times_normal = db.Column(db.Integer(), nullable=True)
    is_active = db.Column(db.Boolean, default=True, nullable=True)
    start_date = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=True)
    end_date = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f"<LoyaltyProductRule (id={self.id})>"
