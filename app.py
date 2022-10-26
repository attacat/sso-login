import json
import os
from decouple import config
from flask_mysqldb import MySQL



from flask import Flask, redirect, request, url_for, render_template, flash

from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from oauthlib.oauth2 import WebApplicationClient
import requests

from db import init_db_command
from user import User
import pymysql



#To run create a OAuth client ID on Google developers credentails page and set env variable of the client_id and the client_secret
GOOGLE_CLIENT_ID = config("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = config("GOOGLE_CLIENT_SECRET")
GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)
# add error handling to the Google API call,
# just in case Google’s API returns a failure and not the valid provider configuration document.
def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'attacat_360'
 
mysql = MySQL(app)

with app.app_context():
    cursor = mysql.connection.cursor()
    variable = cursor.execute('''SELECT * FROM attacat_360.roles;''')
    print(variable)


    mysql.connection.commit()
    cursor.close()





app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)




login_manager = LoginManager()
login_manager.init_app(app)

client = WebApplicationClient(GOOGLE_CLIENT_ID)





@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)




@app.route("/")
def index():
    if current_user.is_authenticated:
        return render_template("base.html")
    else:
        return render_template("login.html")


@app.route("/login")
def login():
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri= request.base_url + "/callback",
        scope=["openid", "email", "profile"],
    )
    return redirect(request_uri)


@app.route("/login/callback")
def callback():
    code = request.args.get("code")

    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]

    token_url, headers, body = client.prepare_token_request(
    token_endpoint,
    authorization_response=request.url,
    redirect_url=request.base_url,
    code=code
    )
    token_response = requests.post(
    token_url,
    headers=headers,
    data=body,
    auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
    )

    client.parse_request_body_response(json.dumps(token_response.json()))

    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)
    # if userinfo_response.json()["hd"] != "attacat.co.uk":
    #     flash("User email not eligible to sign into the website.")
    #     return "User email not eligible to sign into the website.", 403
    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()["sub"]
        users_email = userinfo_response.json()["email"]
        picture = userinfo_response.json()["picture"]
        users_name = userinfo_response.json()["given_name"]
    else:
        return "User email not available or not verified by Google.", 400

    user = User(
        id_=unique_id, name=users_name, email=users_email, profile_pic=picture
    )

    if not User.get(unique_id):
        User.create(unique_id, users_name, users_email, picture)

    login_user(user)

    return redirect(url_for("index"))


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/set-date")
@login_required
def set_date():
    return render_template("set_date.html")

@app.route("/select_reviewers")
@login_required
def select_reviewers():
    return render_template("select_reviewers.html")

@app.route("/reviews-to-complete")
@login_required
def reviews_to_complete():
    return render_template("reviews_to_complete.html")

@app.route("/my-feedback")
@login_required
def my_feedback():
    return render_template("my_feedback.html")

@app.route("/guidelines")
@login_required
def guidelines():
    return render_template("guidelines.html")

@app.route("/admin")
@login_required
def admin():
    if not current_user.role =="Owner":
        flash("You do not have access to view this page.")
        return redirect(url_for('guidelines'))
    else: 
        return render_template("add_user.html")


if __name__ == "__main__":
    app.run(ssl_context="adhoc")