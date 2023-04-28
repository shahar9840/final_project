from controllers.managers import manager_login,manager_main,create_category,create_dish,orders_manage,show_categories,delete_category,show_dishes,delete_dish,dishes_by_category,edit_dish,show_order,clean_order,edit_category
from flask import Blueprint

managers_bp = Blueprint('managers',__name__)

managers_bp.add_url_rule('/managers/login',view_func=manager_login,methods=['GET','POST'])
managers_bp.add_url_rule('/managers/main',view_func=manager_main,methods=['GET','POST'])
managers_bp.add_url_rule('/managers/create_category',view_func=create_category,methods=['GET','POST'])
managers_bp.add_url_rule('/managers/edit_category/<int:id>',view_func=edit_category,methods=['GET','POST'])
managers_bp.add_url_rule('/managers/all_categories',view_func=show_categories,methods=['GET','POST'])
managers_bp.add_url_rule('/managers/all_categories/delete/category/<int:id>',view_func=delete_category,methods=['GET','POST'])
managers_bp.add_url_rule('/managers/all_dishes',view_func=show_dishes,methods=['GET','POST'])
managers_bp.add_url_rule('/managers/category/<int:id>',view_func=dishes_by_category,methods=['GET','POST'])
managers_bp.add_url_rule('/managers/dish/<int:id>/delete',view_func=delete_dish,methods=['GET','POST'])
managers_bp.add_url_rule('/managers/dish/<int:id>/edit',view_func=edit_dish,methods=['GET','POST'])
managers_bp.add_url_rule('/managers/dishes',view_func=create_dish,methods=['GET','POST'])
managers_bp.add_url_rule('/managers/orders',view_func=orders_manage,methods=['GET','POST'])
managers_bp.add_url_rule('/managers/orders/show_order/<int:id>',view_func=show_order,methods=['GET','POST'])
managers_bp.add_url_rule('/managers/orders/clean_order/<int:id>',view_func=clean_order,methods=['GET','POST'])


