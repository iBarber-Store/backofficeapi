from flask import Blueprint
from app.config.api import api_version

branch_office_bp = Blueprint("branchOffice", __name__, url_prefix="/api/"+api_version)

from app.api.branch_office import routes