from db import db
from datetime import datetime as dt
#מודל משלוחים מקושר לעגלה ביחיד ליחיד 
class Delivery(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'), unique=True)
    is_delivered = db.Column(db.Boolean, default=False)
    address = db.Column(db.String(200),default='')
    comment = db.Column(db.Text,default='')
    created = db.Column(db.Date)