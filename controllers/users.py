from flask import render_template, redirect,request,url_for,flash
from flask_login import login_user,current_user,login_required,logout_user
from models.users import User
from models.carts import Cart
from models.deliveries import Delivery
from form_signup import SignUpForm
from form_login import LoginForm
from db import db
from auth import login_manager
from sqlalchemy.exc import IntegrityError

        
#טופס הרשמה 
def signup():
    form= SignUpForm()
    users = User.query.all()
    if request.method == 'POST' and form.validate_on_submit():
        if len(users) > 0 :#במידה ויש יותר ממשתמש אחד במערכת מבצע בדיקה האם יש שם משתמש כזה כבר
            try:
                for user in users:
                    if str(user.username) != str(form.username.data) and str(form.confirm_password.data) == str(form.password.data):  
                            new_user = User(
                                username=form.username.data,
                                password=form.password.data,
                                first_name=form.first_name.data,
                                last_name=form.last_name.data,
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
                    

                    
            except IntegrityError:
                db.session.rollback()
                flash('user name is already taken','not_avalible')                    
                return redirect(url_for('users.signup'))
        else:#במידה וזה משתמש ראשון במערכת
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
#התחברות לקוח
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
#התחברות לקוח 
@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('users.login'))
#טופס התחברות לקוח
def login():
    form = LoginForm() 
    if current_user.is_authenticated:
        return redirect(url_for('main.main'))
    if request.method == "POST":
        remember=False
        if form.remember_me.data == True:
            remember=True
        user = User.query.filter_by(username=form.username.data).first()
        if user != None :
            if form.password.data == user.password :
                login_user(user,remember=remember)  
                flash('loged','loged')
                return redirect(url_for('users.login'))
            else:
                flash('wrong password please try again','wrong_password')
                return redirect(url_for('users.login'))
    return render_template('before_login/login.html',form=form)
#התנתקות משתמש
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.main'))
#שינוי פרטי משתמש
@login_required
def change_details():
    form=SignUpForm()
    user=current_user
    if request.method == 'POST' and  form.validate_on_submit():
        if str(form.confirm_password.data) == str(form.password.data) and user.username == form.username.data:#במידה והשם משתמש נשאר אותו השם
            user.first_name=form.first_name.data
            user.last_name = form.last_name.data
            user.password = form.password.data
            user.email = form.email.data
            user.carts[-1].deliveries.address = form.address.data
            db.session.commit()
            flash('details has been change!','details_changed')
            return redirect(url_for('main.main'))
        elif  str(form.confirm_password.data) == str(form.password.data):#במידה ובוצע שינוי על השם משתמש 
            user.first_name=form.first_name.data
            user.last_name = form.last_name.data
            user.username =form.username.data
            user.password = form.password.data
            user.email = form.email.data
            user.carts[-1].deliveries.address = form.address.data
            db.session.commit()
            flash('details has been change!','details_changed')
            return redirect(url_for('main.main'))
        else:
            flash('details has not chaned!','details_not_changed')
            return redirect(url_for('main.main'))
    return render_template('after_login/change_details.html',user=user,form=form)
    