import os


# TODO: Config validation
class Config(object):
    DATABASE_URI = 'mysql://user@localhost/foo'
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    AUTH_TOKEN_EXP_IN_SEC = int(os.environ.get("AUTH_TOKEN_EXP_IN_SEC"))
    AUTH_SECRET = os.environ.get("AUTH_SECRET")
    AUTH_ALGORITHM = os.environ.get("AUTH_ALGORITHM")
    TRANSACTION_TOKEN_EXP_IN_SEC = int(os.environ.get("TRANSACTION_TOKEN_EXP_IN_SEC"))
    TRANSACTION_SECRET = os.environ.get("TRANSACTION_SECRET")
    TRANSACTION_ALGORITHM = os.environ.get("TRANSACTION_ALGORITHM")


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


config_by_name = dict(
    dev=DevelopmentConfig,
    prod=ProductionConfig
)
