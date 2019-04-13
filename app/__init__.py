import os
from flask import Flask, render_template, url_for, redirect
from flask_script import Manager
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app.config import get_config

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

config_name = os.environ.get("FLASK_ENV") or "development"
app.config.from_object(get_config(config_name))

manager = Manager(app)
moment = Moment(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.routes.pages_routes import pages_bp

app.register_blueprint(pages_bp, url_prefix='/')
