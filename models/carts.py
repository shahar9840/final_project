from db import db
from models.users import User

# מודל עגלה המקושר לשם משתמש ברבים ליחיד ,מקושר למשלוחים ביחיד ליחיד ומקושר למנות ברבים לרבים עם מודל מקשר פריטים
class Cart(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    deliveries = db.relationship('Delivery', backref='cart',uselist=False,cascade="save-update")

    
