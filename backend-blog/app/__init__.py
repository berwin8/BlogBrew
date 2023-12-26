# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    # cors = CORS(app, resources={r"/post/*": {"origins": "http://localhost:3000"}})
    CORS(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'

    db.init_app(app)
    migrate = Migrate(app, db)


    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
