from flask import render_template, redirect,request,url_for,flash
from flask_login import LoginManager,UserMixin,login_user,current_user,login_required,logout_user
from models.users import User
from form import Form
from db import db
from auth import login_manager
from sqlalchemy.exc import IntegrityError

        

def signup():
    form= Form()
    users = User.query.all()
    print(users)
    if request.method == 'POST':
        if str(form.confirm_password.data) != str(form.password.data):
                db.session.rollback()
                flash('confirm password must match to password field','unmatch')
                return redirect(url_for('users.signup'))
        
        if len(users) > 0 :
            try:
                for user in users:
                    if str(user.username) != str(form.username.data) and str(form.confirm_password.data) == str(form.password.data):
                            print('not taken')
                            new_user = User(
                                username=form.username.data,
                                password=form.password.data,
                                first_name=form.first_name.data,
                                last_name = form.last_name.data,
                                email=form.email.data
                            )
                            db.session.add(new_user)
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
                flash('loged','loged')
                return redirect(url_for('users.login'))
    return render_template('before_login/login.html',form=form)

@login_required
def logout():
    logout_user()
    return redirect(url_for('main.main'))