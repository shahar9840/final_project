from flask import Flask
from db import db
from models.carts import Cart
from models.category import Category
from models.deliveries import Delivery
from models.dishes import Dish,Dish_Items
from models.users  import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
app.config['SECRET_KEY'] = 'kjhgi1723yt172g'
db.init_app(app)



with app.app_context():
    db.create_all()



if __name__ == "__main__":
    app.run(debug=True)