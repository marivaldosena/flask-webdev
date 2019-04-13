from flask import Blueprint, render_template, url_for, redirect
from app.forms import NameForm

pages_bp = Blueprint('pages', __name__)

@pages_bp.route("/", methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()

    if form.validate_on_submit():
        name = form.name.data
        print(form.name.data)
        form.name.data = ""
        return redirect(url_for("user", name=name))

    return render_template("index.html", form=form, name=name)


@pages_bp.route("/user/<name>", methods=["GET", "POST"])
def user(name):
    return render_template("user.html", name=name)