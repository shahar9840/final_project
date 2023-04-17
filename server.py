from flask import Flask
from db import db
from models.carts import Cart
from models.category import Category
from models.deliveries import Delivery
from models.dishes import Dish,dish_items 

from models.users  import User
from routes.main import main_bp
from routes.users import users_bp
from routes.managers import managers_bp
from auth import login_manager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
app.config['SECRET_KEY'] = 'kjhgi1723yt172g'
db.init_app(app)
login_manager.init_app(app)



with app.app_context():
    db.create_all()

app.register_blueprint(main_bp)
app.register_blueprint(users_bp)
app.register_blueprint(managers_bp)

if __name__ == "__main__":
    app.run(debug=True)