from models.user import User
from flask_mysqldb import MySQL


def get_all_users():
    db = get_db()
    users = db.execute( "SELECT * FROM user").fetchall()
    return users


def get(user_id):
    db = get_db()
    user = db.execute(
        "SELECT * FROM user WHERE id = ?", (user_id,)
    ).fetchone()
    if not user:
        return None

    user = User(
         id_=user[0], name=user[1], email=user[2], profile_pic=user[3]
        )
    return user


def create(id_, name, email, profile_pic):
    db = get_db()
    db.execute(
        "INSERT INTO user (id, name, email, profile_pic)"
        " VALUES (?, ?, ?, ?)",
        (id_, name, email, profile_pic),
    )
    db.commit()

