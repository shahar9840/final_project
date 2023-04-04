from db import db 

class Dish(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    price = db.Column(db.Integer,nullable=False)
    description = db.Column(db.Text,nullable=False)
    imageUrl = db.Column(db.Text,default = '')
    is_gluten_free = db.Column(db.Boolean,default = False)
    is_vegeterian = db.Column(db.Boolean,default = False)
    category_id = db.Column(db.Integer,db.ForeignKey('category.id'))
    items = db.relationship('Items',secondary='dish_items',backref='dishes')


class Dish_Items(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    dish_id = db.Column(db.Integer,db.ForeignKey('dish.id'))
    cart_id = db.Column(db.Integer,db.ForeignKey('cart.id'))
    amount = db.Column(db.Integer,default=1)

