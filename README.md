## Login SSO

## Description
This is a flask app that is designed to work as an api for Google single-sign-on. The user should be able to click and login into a page using their google account and log out. The styling is minimal as it mainly focuses on functionality. This will later on be used as an api and connect with a front-end app that will manage the styling. This is to be modified once a front end application is created. 

## How To Use
* To start the application, clone it to your local device using: gh repo clone attacat/sso-login
* Head to Google developers credentials page and create credentials for )Auth client ID. Create local variables using the client_id and the client_secret. You should be able to do that creating a .env file with those variables.
* Run pip install -r requirements.txt to install all dependancies
* Run python app.py to initiate DB
* Run python app.py again to start the application on your device