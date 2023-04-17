from controllers.managers import manager_login,manager_main,create_category,dish_manage,orders_manage,show_categories
from flask import Blueprint

managers_bp = Blueprint('managers',__name__)

managers_bp.add_url_rule('/managers/login',view_func=manager_login,methods=['GET','POST'])
managers_bp.add_url_rule('/managers/main',view_func=manager_main,methods=['GET','POST'])
managers_bp.add_url_rule('/managers/create_category',view_func=create_category,methods=['GET','POST'])
managers_bp.add_url_rule('/managers/all_categories',view_func=show_categories,methods=['GET','POST'])
managers_bp.add_url_rule('/managers/dishes',view_func=dish_manage,methods=['GET','POST'])
managers_bp.add_url_rule('/managers/orders',view_func=orders_manage,methods=['GET','POST'])


