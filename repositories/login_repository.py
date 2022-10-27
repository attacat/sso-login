from app import app
from db_connector import db_connector



def look_for_email_in_mysql(email):
    #might need to add different quotes ''' '''
    result = db_connector(app, f'SELECT * FROM attacat_360.users WHERE email = {email};')
    return result

def add_user_from_db_as_object(email):
    results = db_connector(app, f'SELECT * FROM attacat.user WHERE email = {email}').fetchone()
    #take elements from the database to create an object figure out what is the object that the code above generates
    



