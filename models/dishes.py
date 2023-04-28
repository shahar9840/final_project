from db import db 


class Dish(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    price = db.Column(db.Integer,nullable=False)
    description = db.Column(db.Text,nullable=False)
    imageUrl = db.Column(db.Text,default='')
    is_gluten_free = db.Column(db.Boolean,default=False)
    is_vegeterian = db.Column(db.Boolean,default=False)
    category_id = db.Column(db.Integer,db.ForeignKey('category.id'))
    categories = db.relationship('Category',backref='dishes',cascade="save-update")

class Items(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    dish_id=db.Column(db.Integer,db.ForeignKey('dish.id'))
    cart_id=db.Column(db.Integer,db.ForeignKey('cart.id'))
    amount = db.Column(db.Integer,default=1)
    dishes = db.relationship('Dish',backref='items',cascade="save-update")
    items = db.relationship('Cart',backref='items',cascade="save-update")


