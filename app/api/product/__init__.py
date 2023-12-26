from flask import Blueprint
from app.config.api import api_version

product_bp = Blueprint("product", __name__, url_prefix="/api/"+api_version)

from app.api.product import routes