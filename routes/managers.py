from controllers.managers import manager_login,manager_main,create_category,create_dish,orders_manage,show_categories,delete_category,show_dishes,delete_dish,dishes_by_category,edit_dish,show_order,clean_order,edit_category,delivery_deliverd,show_users,make_staff,remove_staff
from flask import Blueprint

managers_bp = Blueprint('managers',__name__)

managers_bp.add_url_rule('/managers/login',view_func=manager_login,methods=['GET','POST'])
managers_bp.add_url_rule('/managers/main',view_func=manager_main)
managers_bp.add_url_rule('/managers/show_users',view_func=show_users)
managers_bp.add_url_rule('/managers/make_staff/<int:id>',view_func=make_staff)
managers_bp.add_url_rule('/managers/remove_staff/<int:id>',view_func=remove_staff)
managers_bp.add_url_rule('/managers/create_category',view_func=create_category,methods=['GET','POST'])
managers_bp.add_url_rule('/managers/edit_category/<int:id>',view_func=edit_category,methods=['GET','POST'])
managers_bp.add_url_rule('/managers/show_categories',view_func=show_categories)
managers_bp.add_url_rule('/managers/delete/category/<int:id>',view_func=delete_category)
managers_bp.add_url_rule('/managers/show_dishes',view_func=show_dishes)
managers_bp.add_url_rule('/managers/category/<int:id>',view_func=dishes_by_category)
managers_bp.add_url_rule('/managers/delete/dish/<int:id>',view_func=delete_dish)
managers_bp.add_url_rule('/managers/edit/dish/<int:id>',view_func=edit_dish,methods=['GET','POST'])
managers_bp.add_url_rule('/managers/create_dish',view_func=create_dish,methods=['GET','POST'])
managers_bp.add_url_rule('/managers/orders',view_func=orders_manage)
managers_bp.add_url_rule('/managers/orders/show_order/<int:id>',view_func=show_order)
managers_bp.add_url_rule('/managers/orders/delivery_delivered/<int:id>',view_func=delivery_deliverd)
managers_bp.add_url_rule('/managers/orders/clean_order/<int:id>',view_func=clean_order)


