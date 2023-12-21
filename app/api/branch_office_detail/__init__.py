from flask import Blueprint
from app.config.api import api_version

branch_office_detail_bp = Blueprint("branch_office_detail", __name__, url_prefix="/api/"+api_version)

from app.api.branch_office_detail import routes