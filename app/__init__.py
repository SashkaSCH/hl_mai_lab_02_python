from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)
    ma.init_app(app)

    with app.app_context():
        from . import models
        db.create_all()

        from app.resources import setup_routes
        setup_routes(app)

    return app
