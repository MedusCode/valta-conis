from flask import Blueprint

wallet_blueprint = Blueprint('wallet', __name__)

from .wallet_controller import *
