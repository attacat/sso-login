from flask import Flask
from controller import blueprint
from db_connector import db_connector
from login import set_login_manager


app = Flask(__name__)

connection = db_connector(app)
print(connection)
# login_manager = set_login_manager(app)

# app.register_blueprint(blueprint)



if __name__ == "__main__":
    app.run(ssl_context="adhoc")