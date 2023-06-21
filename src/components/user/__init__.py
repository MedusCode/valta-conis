from flask import Blueprint

user_blueprint = Blueprint('user', __name__)

from .user_controller import *