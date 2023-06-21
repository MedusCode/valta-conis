from src import db
from src.components.loyalty_product_rule.loyalty_product_rule_model import LoyaltyProductRule
from src.components.order_product.order_product_model import OrderProduct
from src.helpers.sqlalchemy.base_model import BaseModel

class Product(BaseModel):
    __tablename__ = "valta_product"

    product_integration_id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(255), unique=False, nullable=True)
    vendor_code = db.Column(db.String(50), unique=True, nullable=False)
    barcode = db.Column(db.String(255), unique=True, nullable=False)
    present_for_vet = db.Column(db.Boolean, default=False, nullable=False)
    valid_for_loyalty = db.Column(db.Boolean, default=False, nullable=False)
    order_products = db.relationship(OrderProduct)
    # loyalty_product_rules = db.relationship(LoyaltyProductRule)

    def __repr__(self):
        return f"<Product (product_integration_id={self.product_integration_id})>"
