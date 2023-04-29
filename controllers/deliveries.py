from flask import render_template, redirect,request,url_for,flash
from flask_login import current_user,login_required
from db import db
from models.carts import Cart
from models.deliveries import Delivery
from form_order import OrderForm
from controllers.cart import show_order
from datetime import datetime as dt

#טופס ביצוע הזמנה הכנסת כתובת אם שונה והערות למשלוח
@login_required
def order_form(id):
    form=OrderForm()
    now=dt.now()
    delivery=current_user.carts[-1].deliveries
    print(form.validate_on_submit())
    if request.method == 'POST' and form.validate_on_submit():
        delivery.address = form.address.data
        delivery.comment = form.comment.data
        delivery.created = now
        db.session.commit()
        return redirect(url_for('deliveries.order_confirm',id=delivery.id))   
    return render_template('after_login/order_form.html',delivery=delivery,form=form,show_order=show_order())

#פרטי הזמנה שבוצעה ואישור
@login_required
def order_confirm(id):
    cart_price=sum([item.dishes.price for item in show_order()])
    delivery = Delivery.query.get(id)
    new_cart=Cart(
        user_id = current_user.id
        )
    db.session.add(new_cart)
    db.session.commit()
    new_delivery = Delivery(
        cart_id=new_cart.id,
        address= delivery.address,
        comment=''
    )
    db.session.add(new_delivery)
    db.session.commit()
    return render_template('after_login/order_confirm.html',delivery=delivery,cart_price=cart_price)

#צפייה בכל ההזמנות של הלקוח המחובר
@login_required
def order_history():
    carts = current_user.carts
    price = [[price.dishes.price for price in cart.items] for cart in carts]  
    return render_template('after_login/order_history.html',carts=carts,price=price)