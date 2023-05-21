import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .views import views_blueprint


# Initialize the db and migrate objects
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../config.py'))
    app.register_blueprint(views_blueprint)
    # Bind the app object to the db and migrate objects
    db.init_app(app)
    migrate.init_app(app, db)

    return app



