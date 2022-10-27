from flask import Blueprint, render_template
from flask_login import login_required

general_menu_blueprint = Blueprint("general_menu_blueprint", __name__)

@general_menu_blueprint.route("/set-date")
@login_required
def set_date():
    return render_template("set_date.html")

@general_menu_blueprint.route("/select_reviewers")
@login_required
def select_reviewers():
    return render_template("select_reviewers.html")

@general_menu_blueprint.route("/reviews-to-complete")
@login_required
def reviews_to_complete():
    return render_template("reviews_to_complete.html")

@general_menu_blueprint.route("/my-feedback")
@login_required
def my_feedback():
    return render_template("my_feedback.html")

@general_menu_blueprint.route("/guidelines")
@login_required
def guidelines():
    return render_template("guidelines.html")