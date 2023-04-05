from db import db
from datetime import datetime as dt

class Delivery(db.Model):
    id = db.Column(db.Integer,db.ForeignKey('delivery.id'),primary_key=True )
    # cart_id = db.Column(db.Integer,db.ForeigKey('cart.id'))
    is_delivered = db.Column(db.Boolean,default=False)
    address = db.Column(db.String(200),nullable=False)
    comment = db.Column(db.Text)
    created = db.Column(db.Date,default=dt.now)