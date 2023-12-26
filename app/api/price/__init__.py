from flask import Blueprint
from app.config.api import api_version

price_bp = Blueprint("price", __name__, url_prefix="/api/"+api_version)

from app.api.price import routes