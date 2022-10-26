from app import app
from flask_mysqldb import MySQL
import requests
from models.user import User
import os
from app import app
from flask_login import (
    LoginManager,
    current_user)
from decouple import config
from oauthlib.oauth2 import WebApplicationClient


login_manager = LoginManager()
login_manager.init_app(app)

client = WebApplicationClient(GOOGLE_CLIENT_ID)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


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