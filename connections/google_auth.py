import requests
from decouple import config
import os
from oauthlib.oauth2 import WebApplicationClient


#Google connection
#Google connection
#To run create a OAuth client ID on Google developers credentails page and set env variable of the client_id and the client_secret
GOOGLE_CLIENT_ID = config("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = config("GOOGLE_CLIENT_SECRET")
GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration")
client = WebApplicationClient(GOOGLE_CLIENT_ID)


# add error handling to the Google API call,
# just in case Google’s API returns a failure and not the valid provider configuration document.
def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()

def generate_secret_key(app):
    app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)
    return app.secret_key