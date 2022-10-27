# from user import User
import json


from flask import  redirect, request, url_for, render_template, flash, Blueprint

from flask_login import (
    login_required,
    login_user,
    logout_user,
)
import requests

from models.user import User


blueprint = Blueprint("blueprint", __name__)











