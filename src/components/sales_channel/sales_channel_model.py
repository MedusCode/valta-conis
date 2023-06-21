import uuid

from sqlalchemy import UUID

from src import db
from src.components.loyalty_product_rule.loyalty_product_rule_model import LoyaltyProductRule
from src.components.user.user_model import User
from src.helpers.sqlalchemy.base_model import BaseModel


class SalesChannel(BaseModel):
    __tablename__ = "sales_channel"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    sales_channel_integration_id = db.Column(db.String(50), primary_key=True, unique=True)
    is_able_to_sell = db.Column(db.Boolean, default=False, nullable=False)
    name = db.Column(db.String(250), nullable=True)
    users = db.relationship(User)
    loyalty_product_rules = db.relationship(LoyaltyProductRule)

    def __repr__(self):
        return f"<SalesChannel (id={self.id})>"
