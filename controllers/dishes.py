from flask import render_template, redirect,request,url_for,flash
from flask_login import current_user,login_required
from db import db
from sqlalchemy.exc import IntegrityError
from models.category import Category
from models.dishes import Dish
from from_addtocart import AddToCartForm
from controllers.cart import add_to_cart

#צפייה בכל המנות במסעדה
@login_required
def show_dishes():
    form=AddToCartForm()
    dishes = Dish.query.all()
    return render_template('after_login/show_dishes.html',dishes=dishes,form=form)
#צפייה במנה ספציפית
@login_required
def show_dish(id):
    dish=Dish.query.get(id)
    return render_template('after_login/show_dish.html',dish=dish)