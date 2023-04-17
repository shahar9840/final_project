from flask import render_template, redirect,request,url_for
from models.users import User
from flask_login import current_user


def main():
    if current_user.is_authenticated:
        greeting = f'{current_user.first_name.capitalize()} { current_user.last_name.capitalize()}'
        return render_template('after_login/main.html',greeting=greeting)
    else:
        greeting = 'Guest'
        return render_template('before_login/main.html',greeting=greeting)