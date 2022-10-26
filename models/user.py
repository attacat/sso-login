from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id_user, full_name, email, added, status, updated, update_user, role):
        self.id_user = id_user
        self.full_name = full_name
        self.email = email
        self.added = added,
        self.status = status
        self.updated = updated
        self.update_user = update_user
        self.role = role
