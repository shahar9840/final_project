from flask import render_template, redirect,request,url_for,flash
from flask_login import current_user,login_required
from db import db
from models.carts import Cart
from models.deliveries import Delivery
from form_order import OrderForm
from controllers.cart import show_order
from datetime import datetime as dt


@login_required
def order_form(id):
    form=OrderForm()
    now=dt.now()
    print(now)
    delivery=current_user.carts[-1].deliveries
    print(delivery.is_delivered)
    if request.method == 'POST' and form.validate_on_submit():
        delivery.address = form.address.data
        delivery.comment = form.comment.data
        delivery.created = now
        delivery.is_delivered = True
        db.session.commit()
        return redirect(url_for('deliveries.order_confirm',id=delivery.id))
    
    return render_template('after_login/order_form.html',delivery=delivery,form=form,show_order=show_order())

@login_required
def order_confirm(id):
    cart_price=sum([item.dishes.price for item in show_order()])
    delivery = Delivery.query.get(id)
    if delivery.is_delivered:
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