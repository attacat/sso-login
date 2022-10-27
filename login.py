from models.user import User
from flask import Blueprint
from google_auth import get_google_provider_cfg, client, GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET
from flask import redirect, request, url_for, render_template
import requests
import json
from repositories.login_repository import look_for_email_in_mysql

from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user
)


def set_login_manager(app):
    login_manager = LoginManager()
    login_manager.init_app(app)


login_blueprint = Blueprint("login_blueprint", __name__)

@login_blueprint.route("/")
def index():
    if current_user.is_authenticated:
        return render_template("base.html")
    else:
        return render_template("login.html")

@login_blueprint.route("/login")
def login():
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri= request.base_url + "/callback",
        scope=["openid", "email", "profile"],
    )
    return redirect(request_uri)


@login_blueprint.route("/login/callback")
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
    if userinfo_response.json().get("email_verified") :
        users_email = userinfo_response.json()["email"]
        users_name = userinfo_response.json()["given_name"]
        result = look_for_email_in_mysql(users_email)
        if result == 0:
            return "User is not authorised to enter the website", 400
        
    else:
        return "User email not available or not verified by Google.", 400

    #Code below needs work as it needs to populate user object with data from the db
    user = User(
        name=users_name, email=users_email,
    )
    #Should get id as an arguement
    if not User.get():
        User.create(users_name, users_email)

    login_user(user)

    return redirect(url_for("index"))