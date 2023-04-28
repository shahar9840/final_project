from controllers.categories import dishes_by_category,show_categories
from flask import Blueprint

categories_bp= Blueprint('categories',__name__)

categories_bp.add_url_rule('/categories/category/<int:id>',view_func=dishes_by_category,methods=['GET','POST'])
categories_bp.add_url_rule('/categories/all_categories',view_func=show_categories,methods=['GET','POST'])
