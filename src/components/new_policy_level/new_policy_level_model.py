import uuid

from sqlalchemy import UUID

from src import db
from src.components.loyalty_product_rule.loyalty_product_rule_model import LoyaltyProductRule
from src.components.user.user_model import User
from src.helpers.sqlalchemy.base_model import BaseModel


class NewPolicyLevel(BaseModel):
    __tablename__ = "new_policy_level"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    new_policy_integration_id = db.Column(db.String(50), primary_key=True, unique=True)
    name = db.Column(db.String(250), nullable=True)
    users = db.relationship(User)
    loyalty_product_rules = db.relationship(LoyaltyProductRule)

    def __repr__(self):
        return f"<NewPolicyLevel (id={self.id})>"
