from db import db

class Cart(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    delivery_id=db.Column(db.Integer,db.ForeignKey('delivery.id'))