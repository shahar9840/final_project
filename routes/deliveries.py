from controllers.deliveries import order_form,order_confirm,order_history
from flask import Blueprint

deliveries_bp=Blueprint('deliveries',__name__)

deliveries_bp.add_url_rule('/order/order_form/<int:id>',view_func=order_form,methods=['GET','POST'])
deliveries_bp.add_url_rule('/order/order_history',view_func=order_history)
deliveries_bp.add_url_rule('/order/<int:id>/order_confirm',view_func=order_confirm)
