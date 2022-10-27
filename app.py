import os
from flask import Flask
from login import login_blueprint
from flask_login import LoginManager
from models.user import User
from db_connector import cursor



app = Flask(__name__)

app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(id):
    return User.get(id)


app.register_blueprint(login_blueprint)



if __name__ == "__main__":
    app.run(ssl_context="adhoc")