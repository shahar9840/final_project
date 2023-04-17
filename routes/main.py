from controllers.main import main
from flask import Blueprint
main_bp = Blueprint('main',__name__)

main_bp.add_url_rule('/',view_func=main)



