from flask import Blueprint

branch_bp = Blueprint("branch", __name__)

from app.branch import routes