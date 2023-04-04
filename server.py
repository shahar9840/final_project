from flask import Flask
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
app.config['SECRET_KEY']='342U10FWE'
db.init_app(app)



with app.app_context():
    db.create_all()



# if __name__ == "__main__":
#     app.run(debug=True)