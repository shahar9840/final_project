from flask import render_template, redirect,request,url_for,flash
from flask_login import LoginManager,UserMixin,login_user,current_user,login_required,logout_user
from models.users import User
from models.category import Category
from form import Form
from db import db
from auth import login_manager
from sqlalchemy.exc import IntegrityError


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('managers.manager_login'))




def manager_login():
    form = Form()
    
    if current_user.is_authenticated:
        return redirect(url_for('managers.manager_main'))
    if request.method == "POST":
        print(form.remember_me.data)
        remember=False
        if form.remember_me.data == True:
            remember=True
        user = User.query.filter_by(username=form.username.data).first()
        if user != None :
            if form.password.data == user.password and user.is_staff == True :
                login_user(user,remember=remember)
                flash('logged in successfully!','loged')
                return redirect(url_for('managers.manager_main'))
    
    
    return render_template('manager_templates/manager_login.html',form = form)
    


@login_required
def manager_main():    
    if current_user.is_staff:
        return render_template('manager_templates/manager_main.html')
    else:
        return redirect(url_for('managers.login')) 


@login_required
def create_category():
    form = Form()
    if current_user.is_staff:
        if request.method == "POST":
            new_category = Category(
                name = form.create_category.data,
                imageUrl = form.imageUrl.data
            )
            db.session.add(new_category)
            db.session.commit()
            flash(f'{form.create_category.data.capitalize()} created as new category!','create_new')
            return redirect(url_for('managers.manager_main'))
        return render_template('manager_templates/manager_category.html',form=form)

@login_required
def delete_category():
    form = Form()
    if current_user.is_staff:
        if request.method == "POST":
            pass   
        return render_template('manager_templates/manager_category.html',form=form)
    else:
        return redirect(url_for("main.mainhtd"))

@login_required
def dish_manage():
    if current_user.is_staff:
        return render_template('manager_templates/manager_dishes.html')

@login_required
def orders_manage():
    if current_user.is_staff:
        return render_template('manager_templates/manager_show_orders.html')

@login_required
def show_categories():
    categories = Category.query.all()
    if current_user.is_staff:
        return render_template('manager_templates/show_categories.html',categories = categories)

    