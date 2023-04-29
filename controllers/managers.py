from flask import render_template, redirect,request,url_for,flash
from flask_login import login_user,current_user,login_required
from models.users import User
from models.category import Category
from models.deliveries import Delivery
from models.dishes import Dish
from models.carts import Cart
from form_login import LoginForm
from form_createdish import CreateDishForm
from form_createcategory import CreateCategoryForm
from db import db
from auth import login_manager
from controllers.cart import show_order
from werkzeug.exceptions import BadRequestKeyError


#התחברות מנהל
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
#התחברות מנהל
@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('users.login'))
#התחברות מנהל
def manager_login():
    form = LoginForm()   
    if current_user.is_authenticated:
        return redirect(url_for('managers.manager_main'))
    if request.method == "POST":
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
#צפייה בעמוד ראשי של הניהול
@login_required
def manager_main():
    deliveries=Delivery.query.all()  
    categories = Category.query.all()    
    if current_user.is_staff:
        return render_template('manager_templates/manager_main.html',categories=categories,deliveries=deliveries)
    else:
        return redirect(url_for('main.main'))
#הוספת קטגוריה
@login_required
def create_category():
    form = CreateCategoryForm()
    if current_user.is_staff:
        if request.method == "POST" and form.validate_on_submit():
            new_category = Category(
                name = form.create_category.data,
                imageUrl = form.imageUrl.data
            )
            db.session.add(new_category)
            db.session.commit()
            flash(f'{form.create_category.data.capitalize()} created as new category!','create_new')
            return redirect(url_for('managers.show_categories'))
        return render_template('manager_templates/create_category.html',form=form)
#צפייה בכל הקטגוריות
@login_required
def show_categories():
    categories = Category.query.all()
    if current_user.is_staff:
        return render_template('manager_templates/show_categories.html',categories = categories)
#עריכת קטגוריה
@login_required
def edit_category(id):
    form=CreateCategoryForm()
    category = Category.query.get(id)
    if current_user.is_staff:
        if request.method =="POST":
            category.name = form.name.data
            category.imageUrl = form.imageUrl.data
            db.session.commit()
        return render_template('manager_templates/edit_category.html',category=category,form=form)
#מחיקת קטגוריה
@login_required
def delete_category(id):
    if current_user.is_staff:
        category= Category.query.get(id)
        db.session.delete(category)
        db.session.commit()
        flash(f'{category.name} has been deleted','deleted')
        return redirect(url_for('managers.show_categories'))
#יצירת מנה 
@login_required
def create_dish():
        form = CreateDishForm()
        categories=Category.query.all()
        if current_user.is_staff:
            if request.method == "POST" and form.validate_on_submit():
                new_dish = Dish(
                    name=form.dish_name.data,
                    price=form.price.data,
                    description=form.description.data,
                    imageUrl=form.imageUrl.data,
                    is_gluten_free = form.is_gluten_free.data,
                    is_vegeterian = form.is_vegeterian.data,
                    category_id = request.form['select_categories']
                )
                db.session.add(new_dish)
                try:  
                    db.session.commit()
                    return redirect(url_for('managers.show_dishes'))
                except BadRequestKeyError:
                    flash('אנא בחר קטגוריה למנה','choose')
                    return redirect(url_for('managers.create_dish'))
            return render_template('manager_templates/create_dish.html',form=form,categories=categories)
    
#צפייה בכל המנות
@login_required
def show_dishes():
    dishes = Dish.query.all()
    if current_user.is_staff:
        return render_template('manager_templates/show_dishes.html',dishes=dishes)
#עריכת מנה   
@login_required
def edit_dish(id):
    form = CreateDishForm()
    dish = Dish.query.get(id)
    categories = Category.query.all()
    if current_user.is_staff:
        if request.method == "POST":
            dish.category_id= request.form['select_categories']
            dish.name=form.dish_name.data
            dish.price=form.price.data
            dish.description=form.description.data
            dish.is_gluten_free =form.is_gluten_free.data
            dish.is_vegeterian =form.is_vegeterian.data
            dish.imageUrl = form.imageUrl.data
            db.session.commit()
            return redirect(url_for('managers.dishes_by_category',id=dish.category_id))             
        return render_template('manager_templates/edit_dish.html',dish=dish,form=form,categories=categories)
#מחיקת מנה
@login_required
def delete_dish(id):
    dish= Dish.query.get(id)
    if current_user.is_staff:
        db.session.delete(dish)
        db.session.commit()
        flash(f'{dish.name} has been deleted','deleted_dish')
        return redirect(url_for('managers.show_categories'))    
    
#ניהול כל ההזמנות
@login_required
def orders_manage():
    deliveries=Delivery.query.all()              
    if current_user.is_staff:
        return render_template('manager_templates/manager_show_orders.html',deliveries=deliveries)
#צפייה במנות לפי קטגוריה
@login_required
def dishes_by_category(id):
    category= Category.query.get(id)
    dishes = Dish.query.filter_by(category_id=id).all()
    if current_user.is_staff:
        return render_template('manager_templates/dishes_by_category.html',dishes=dishes,category=category)
#צפייה בהזמנה ספציפית
@login_required
def show_order(id):
    delivery= Delivery.query.get(id)
    cart_price=sum([item.dishes.price for item in delivery.cart.items])
    if current_user.is_staff:
        return render_template('manager_templates/show_order.html',delivery=delivery,cart_price=cart_price)
#מחיקת הזמנה
@login_required
def clean_order(id):
    delivery= Delivery.query.get(id)
    delivery.cart.items=[]
    db.session.commit()
    return redirect(url_for('managers.manager_main'))

@login_required
def delivery_deliverd(id):
    delivery=delivery = Delivery.query.get(id)
    delivery.is_delivered = True
    db.session.commit()
    flash('נשלח','deliverd')
    return redirect(url_for('managers.show_order'))


@login_required
def show_users():
    users=User.query.all()
    if current_user.is_staff:
        return render_template('manager_templates/show_users.html',users=users)

@login_required
def make_staff(id):
    user= User.query.get(id)
    user.is_staff = True
    db.session.commit()
    flash(f'{user.first_name} is staff now','make_staff')
    return redirect(url_for('managers.show_users'))

@login_required
def remove_staff(id):
    user= User.query.get(id)
    user.is_staff = False
    db.session.commit()
    flash(f'{user.first_name} is not staff now','remove_staff')
    return redirect(url_for('managers.show_users'))

