from flask import Blueprint
from app.config.api import api_version

location_bp = Blueprint("location", __name__, url_prefix="/api/"+api_version)

from app.api.location import routes