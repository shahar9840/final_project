from controllers.users import signup,login,logout,change_details
from flask import Blueprint
users_bp = Blueprint('users',__name__)

users_bp.add_url_rule('/users/signup',methods=['GET','POST'],view_func=signup)
users_bp.add_url_rule('/users/change_details',methods=['GET','POST'],view_func=change_details)
users_bp.add_url_rule('/users/login',methods=['GET','POST'],view_func=login)
users_bp.add_url_rule('/users/logout',view_func=logout)
