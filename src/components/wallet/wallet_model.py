import uuid
from datetime import datetime, timezone, timedelta

import jwt

from sqlalchemy import CheckConstraint, UUID

from src import db
from src.helpers.sqlalchemy.base_model import BaseModel


class Wallet(BaseModel):
    __tablename__ = "wallet"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    vc_balance = db.Column(db.Integer(), default=0, nullable=False)
    vc_service_balance = db.Column(db.Integer(), default=0, nullable=False)
    user = db.relationship('User', backref='wallet', uselist=False)

    __table_args__ = (
        CheckConstraint(vc_balance >= 0, name='check_vc_balance_positive'),
        CheckConstraint(vc_service_balance >= 0, name='check_vc_service_balance_positive'),
        {})

    def generate_token(self, secret, token_exp_in_sec, jwt_algorithm):
        return jwt.encode(
            {"id": str(self.id), "exp": datetime.now(tz=timezone.utc) + timedelta(seconds=token_exp_in_sec)},
            secret,
            algorithm=jwt_algorithm
        )

    def __repr__(self):
        return f"<Wallet (id={self.id})>"
