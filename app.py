import os
from flask import Flask
from controllers.login_controller import login_blueprint
from controllers.general_menu_controller import general_menu_blueprint
from flask_login import LoginManager
from models.user import User


app = Flask(__name__)

app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)

login_manager = LoginManager()
login_manager.init_app(app)

# Flask-Login helper to retrieve a user from db
@login_manager.user_loader
def load_user(id_user):
    return User.get(id_user)


app.register_blueprint(login_blueprint)
app.register_blueprint(general_menu_blueprint)


if __name__ == "__main__":
    app.run(ssl_context="adhoc")