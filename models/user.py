from flask_login import UserMixin
from connections.db_connector import cursor

class User(UserMixin):
    def __init__(self, id, full_name, email, added, status, updated, update_user, role):
        self.id = id
        self.full_name = full_name
        self.email = email
        self.added = added,
        self.status = status
        self.updated = updated
        self.update_user = update_user
        self.role = role

    @staticmethod
    def get(id_user):
        list_user_id = [id_user]
        cursor.execute(
        "SELECT * FROM users WHERE id_user = %s", (list_user_id))
        user = cursor.fetchone()
        if not user:
            return None

        user = User(
            id=user[0], full_name=user[1], email=user[2], added = user[3], status= user[4], updated = user[5], update_user = user[6], role = user[7]
        )
        return user