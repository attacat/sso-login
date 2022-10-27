from flask import Flask
from controller import blueprint
from db_connector import db



app = Flask(__name__)

cursor = db.cursor()

cursor.execute("SELECT * FROM attacat_360.users")
tables = cursor.fetchall()
#object type of tables: list
print(type(tables))
# login_manager = set_login_manager(app)

# app.register_blueprint(blueprint)



if __name__ == "__main__":
    app.run(ssl_context="adhoc")