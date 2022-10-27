from models.user import User
from db_connector import db


def get_all_users():
    users = db.execute( "SELECT * FROM user").fetchall()
    return users


def get_user_by_email(email):
    user = db.execute(
        "SELECT * FROM user WHERE email = ?", (email)
    ).fetchone()
    if not user:
        return None

    user = User(
         id=user[0], name=user[1], email=user[2], added = user[3], status= user[4], updated = user[5], update_user = user[6], role = user[7]
        )
    return user

#At the moment we don't need to create a user
def create(id_, name, email, profile_pic):
    db.execute(
        "INSERT INTO user (id, name, email, profile_pic)"
        " VALUES (?, ?, ?, ?)",
        (id_, name, email, profile_pic),
    )
    db.commit()

