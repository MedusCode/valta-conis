import uuid
from datetime import datetime, timezone, timedelta

import jwt

import bcrypt
from sqlalchemy import UUID

from src import db
from src.helpers.sqlalchemy.base_model import BaseModel


class User(BaseModel):
    __tablename__ = "user"

    user_integration_id = db.Column(db.String(50), primary_key=True)
    login = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=True)
    password_hash = db.Column("password", db.String(60), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    second_name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(20), unique=True, nullable=False)
    wallet_id = db.Column(UUID(as_uuid=True), db.ForeignKey('wallet.id'), unique=True, nullable=False)
    sales_channel_integration_id = db.Column(
        db.String(50),
        db.ForeignKey('sales_channel.sales_channel_integration_id'),
        nullable=False
    )
    new_policy_integration_id = db.Column(
        db.String(50),
        db.ForeignKey('new_policy_level.new_policy_integration_id'),
        nullable=False
    )

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        bytes_password = password.encode('utf-8')
        salt = bcrypt.gensalt()

        self.password_hash = bcrypt.hashpw(bytes_password, salt).decode("utf-8")

    def check_password(self, password):
        bytes_password = password.encode('utf-8')
        bytes_password_hash = self.password_hash.encode('utf-8')

        return bcrypt.checkpw(bytes_password, bytes_password_hash)

    def encode_jwt(self, secret, token_exp_in_sec, jwt_algorithm):
        return jwt.encode(
            {
                "id": str(self.user_integration_id),
                "exp": datetime.now(tz=timezone.utc) + timedelta(seconds=token_exp_in_sec)
             },
            secret,
            algorithm=jwt_algorithm
        )

    def __repr__(self):
        return f"<User (user_integration_id={self.user_integration_id})>"
