from flask import render_template
from models.users import User
from models.category import Category

from controllers.cart import show_order
from flask_login import current_user

#צפייה בעמוד ראשי
def main():
    categories = Category.query.all()
    loged=current_user.is_authenticated 
    if not loged:
        greeting = 'Guest'
    else:
        greeting = f'{current_user.first_name.capitalize()} { current_user.last_name.capitalize()}'
        
    return render_template('after_login/main.html',greeting=greeting,categories=categories,loged=loged,show_order=show_order())
    



        