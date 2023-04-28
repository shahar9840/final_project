from db import db
from flask_login import LoginManager,UserMixin,login_user,current_user,login_required,logout_user

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),nullable=False,unique=True)
    password = db.Column(db.String(20),nullable=False)
    first_name = db.Column(db.String(50),nullable=False)
    last_name = db.Column(db.String(50),nullable=False)
    is_staff = db.Column(db.Boolean,default=False)
    email = db.Column(db.String(200),nullable=False)
    carts = db.relationship('Cart', backref='user',cascade="save-update")


    def __str__(self) -> str:
        return self.username
    