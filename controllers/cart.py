from flask import render_template, redirect,request,url_for,flash
from flask_login import current_user,login_required
from db import db
from models.dishes import Dish,Items
from models.carts import Cart
from from_addtocart import AddToCartForm


#הוספה של מנה או יותר לעגלה
@login_required
def add_to_cart(id):
    form=AddToCartForm()
    dish=Dish.query.get(id)
    cart = current_user.carts[-1]
    if request.method == 'POST' and form.validate_on_submit():
        for _ in range(form.amount.data):   
            add_dish=Items(
                dish_id=dish.id,
                cart_id=cart.id 
            )
            db.session.add(add_dish)
            db.session.commit()
        flash(f'נוסף לעגלה {form.amount.data} {dish.name} ' ,'added')
    return redirect(url_for('main.main'))

#צפייה בעגלה האחרונה
@login_required
def show_order():#showing order in main page
    current_cart=current_user.carts[-1]
    last_order=current_cart.items
    return last_order

#צפייה בעגלה
@login_required
def show_cart():
    current_cart=show_order()
    user=current_user
    cart_price=sum([item.dishes.price for item in current_cart])
    cart_id=Cart.query.filter_by(user_id=current_user.id).first().id
    return render_template('after_login/show_cart.html',current_cart=current_cart,user=user,cart_id=cart_id,cart_price=cart_price)

#מחיקת מוצר מהעגלה 
@login_required
def delete_item_from_cart(id):
    item=Items.query.filter_by(dish_id=id).first()
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('cart.show_cart'))


    





    
    