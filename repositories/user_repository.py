from models.user import User
from db_connector import cursor


def get_all_users():
    users = cursor.execute( "SELECT * FROM user").fetchall()
    return users


def get_user_by_email(email):
    list_email = [email]
    cursor.execute(
        "SELECT * FROM users WHERE email = %s", (list_email))
    user = cursor.fetchone()
    print(f'Printing of user in get_user_by_email{user}')
    if not user:
        return None

    user = User(
         id=user[0], full_name=user[1], email=user[2], added = user[3], status= user[4], updated = user[5], update_user = user[6], role = user[7]
        )
    return user
#At the moment we don't need to create a user
# def create(id_, name, email, profile_pic):
#     cursor.execute(
#         "INSERT INTO user (id, name, email, profile_pic)"
#         " VALUES (?, ?, ?, ?)",
#         (id_, name, email, profile_pic),
#     )
#     cursor.commit()

