from controllers.cart import add_to_cart,show_order,show_cart,delete_item_from_cart
from flask import Blueprint

cart_bp=Blueprint('cart',__name__)

cart_bp.add_url_rule('/cart/add_dish/<int:id>',view_func=add_to_cart)
cart_bp.add_url_rule('/cart/show_order/<int:id>',view_func=show_order)
cart_bp.add_url_rule('/cart/show_cart',view_func=show_cart)
cart_bp.add_url_rule('/cart/delete_from_cart/<int:id>',view_func=delete_item_from_cart)