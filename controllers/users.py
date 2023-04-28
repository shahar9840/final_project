from flask import render_template, redirect,request,url_for,flash
from flask_login import LoginManager,UserMixin,login_user,current_user,login_required,logout_user
from models.users import User
from models.dishes import Dish
from models.carts import Cart
from models.deliveries import Delivery
from form import Form
from db import db
from auth import login_manager
from sqlalchemy.exc import IntegrityError

        

def signup():
    form= Form()
    users = User.query.all()
    print(users)
    print(form.errors)

    if request.method == 'POST' :
        print(form.errors)
        if len(users) > 0 :
            try:
                for user in users:
                    if str(user.username) != str(form.username.data) and str(form.confirm_password.data) == str(form.password.data):
                            print('not taken')
                            new_user = User(
                                username=form.username.data,
                                password=form.password.data,
                                first_name=form.first_name.data,
                                last_name=form.last_name.data,
                                email=form.email.data
                            )   
                            print('hi') 
                            db.session.add(new_user)
                            db.session.commit()

                            new_cart=Cart(user_id=new_user.id) 
                            db.session.add(new_cart)    
                            db.session.commit()
                            new_delivery=Delivery(
                                cart_id=new_cart.id,
                                address=form.address.data,
                                comment=''
                            )
                            db.session.add(new_delivery)
                            db.session.commit()
                            flash('signup succsfully','success')
                            return redirect(url_for('users.login'))
                    

                    
            except IntegrityError:
                db.session.rollback()
                flash('user name is already taken','not_avalible')                    
                return redirect(url_for('users.signup'))
        else:
            if str(form.confirm_password.data) == str(form.password.data):
                new_user = User(
                        username=form.username.data,
                        password=form.password.data,
                        first_name=form.first_name.data,
                        last_name = form.last_name.data,
                        email=form.email.data
                    )
                db.session.add(new_user)
                db.session.commit()
                
                new_cart=Cart(user_id=new_user.id) 
                db.session.add(new_cart)    
                db.session.commit()
                new_delivery=Delivery(
                cart_id=new_cart.id,
                address=form.address.data,
                comment=''
                )
                db.session.add(new_delivery)
                db.session.commit()
                flash('signup succsfully','success')
                return redirect(url_for('users.login'))
    return render_template('before_login/signup.html',form=form)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('users.login'))


def login():
    form = Form() 
    if current_user.is_authenticated:
        return redirect(url_for('main.main'))
    if request.method == "POST":
        print(form.remember_me.data)
        remember=False
        if form.remember_me.data == True:
            remember=True
        user = User.query.filter_by(username=form.username.data).first()
        if user != None :
            if form.password.data == user.password :
                login_user(user,remember=remember)
                
                # try:
                #     new_cart=Cart(user_id=user.id)
                #     db.session.add(new_cart)
                #     db.session.commit()
                # except IntegrityError:
                #     db.session.rollback()
                # finally:
                flash('loged','loged')
                return redirect(url_for('users.login'))
    return render_template('before_login/login.html',form=form)

@login_required
def logout():
    logout_user()
    return redirect(url_for('main.main'))


@login_required
def change_details():
    form=Form()

    user=current_user
    if request.method == 'POST':
        if str(form.confirm_password.data) == str(form.password.data):
            user.first_name=form.first_name.data
            user.last_name = form.last_name.data
            user.username = form.username.data
            user.password = form.password.data
            user.email = form.email.data
            user.carts[-1].deliveries.address = form.address.data
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()
                flash('user name is already taken','not_avalible')                    
                return redirect(url_for('users.change_details'))

            flash('details has been change!','details_changed')
            return redirect(url_for('main.main'))
        else:
            flash('details has not chaned!','details_not_changed')
    return render_template('after_login/change_details.html',user=user,form=form)
    