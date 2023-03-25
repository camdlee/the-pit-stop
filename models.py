#------------ IMPORTS --------------
from app import db, login
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


#------------- CLASSES --------------
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable = False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)


    # Hashing our password
    def hash_password(self, original_password):
        return generate_password_hash(original_password)

    # Check password hash
    def check_hash_password(self, login_password):
        return check_password_hash(self.password, login_password)
    
    