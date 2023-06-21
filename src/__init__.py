import os

from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from redis import Redis

from .config import config_by_name
from .middlewares.errors_handler import error_handler

db = SQLAlchemy()
ma = Marshmallow()
r = Redis(host=os.environ.get("REDIS_HOST"), port=os.environ.get("REDIS_PORT"), decode_responses=True)


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    db.init_app(app)
    ma.init_app(app)

    from .components.auth import auth_blueprint
    from .components.user import user_blueprint
    from .components.wallet import wallet_blueprint
    from .components.product import product_blueprint
    app.register_blueprint(auth_blueprint, url_prefix="/")
    app.register_blueprint(user_blueprint, url_prefix="/user")
    app.register_blueprint(wallet_blueprint, url_prefix="/transaction")
    app.register_blueprint(product_blueprint, url_prefix="/product")

    app.register_error_handler(Exception, error_handler)

    return app
