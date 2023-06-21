import os

from flask_migrate import Migrate

from . import create_app, db

app = create_app(os.environ.get('ENV'))

migrate = Migrate(app, db)
