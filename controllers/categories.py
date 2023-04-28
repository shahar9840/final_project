from flask import render_template, redirect,request,url_for,flash
from flask_login import current_user,login_required
from db import db
from sqlalchemy.exc import IntegrityError
from models.category import Category
from models.dishes import Dish


@login_required
def dishes_by_category(id):
    
    category= Category.query.get(id)
    dishes = Dish.query.filter_by(category_id=id).all()
    return render_template('after_login/dishes_by_category.html',dishes=dishes,category=category)

@login_required
def show_categories():
    categories = Category.query.all()
    return render_template('after_login/show_categories.html',categories = categories)