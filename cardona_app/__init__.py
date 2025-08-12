from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db_manager =  SQLAlchemy()

def configure_db(app):
    app.logger.info("SQLITE URI: " + app.config["SQLALCHEMY_DATABASE_URI"])
    db_manager.init_app(app)


def create_app():
    app = Flask(__name__)

    app.config.from_object('config.Config')
    configure_db(app)

    with app.app_context():
        from . import routes_main
        app.register_blueprint(routes_main.main_bp)

    return app
