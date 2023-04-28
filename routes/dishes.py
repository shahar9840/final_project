from controllers.dishes import show_dishes,show_dish
from flask import Blueprint

dishes_bp = Blueprint('dishes',__name__)

dishes_bp.add_url_rule('/all_dishes',view_func=show_dishes,methods=['GET','POST'])
dishes_bp.add_url_rule('/dish/<int:id>',view_func=show_dish,methods=['GET','POST'])