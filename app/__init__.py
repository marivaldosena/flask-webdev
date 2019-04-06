import os
from flask import Flask, render_template, url_for, redirect
from flask_script import Manager
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app.forms import NameForm
from app.config import get_config

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

config_name = os.environ.get("FLASK_ENV") or "development"
app.config.from_object(get_config(config_name))

manager = Manager(app)
moment = Moment(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route("/")
def index():
    name = None
    form = NameForm()

    if form.validate_on_submit():
        name = form.name.data
        print(form.name.data)
        form.name.data = ""
        return redirect(url_for("user", name=name))

    return render_template("index.html", form=form, name=name)


@app.route("/user/<name>", methods=["GET", "POST"])
def user(name):
    return render_template("user.html", name=name)
