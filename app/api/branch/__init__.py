from flask import Blueprint
from app.config.api import api_version

branch_bp = Blueprint("branch", __name__, url_prefix="/api/"+api_version)

from app.api.branch import routes