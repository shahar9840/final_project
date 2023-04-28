from flask import render_template, redirect,request,url_for,flash
from flask_login import current_user,login_required
from db import db
from sqlalchemy.exc import IntegrityError
from models.category import Category
from models.dishes import Dish



@login_required
def show_dishes():
    dishes = Dish.query.all()
    return render_template('after_login/show_dishes.html',dishes=dishes)
@login_required
def show_dish(id):
    dish=Dish.query.get(id)
    return render_template('after_login/show_dish.html',dish=dish)