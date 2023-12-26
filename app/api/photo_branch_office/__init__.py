from flask import Blueprint
from app.config.api import api_version

photo_branch_office_bp = Blueprint("photoBranchOffice", __name__, url_prefix="/api/"+api_version)

from app.api.photo_branch_office import routes