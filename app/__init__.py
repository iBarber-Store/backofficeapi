from flask import Flask
from app.main import main_bp
from app.api.branch import branch_bp
from app.api.branch_office import branch_office_bp
from app.api.branch_office_detail import branch_office_detail_bp
from app.api.location import location_bp
from app.api.photo_branch_office import photo_branch_office_bp
from app.api.product import product_bp
from app.api.price import price_bp

app = Flask(__name__)
app.register_blueprint(main_bp)
app.register_blueprint(branch_bp)
app.register_blueprint(branch_office_bp)
app.register_blueprint(branch_office_detail_bp)
app.register_blueprint(location_bp)
app.register_blueprint(photo_branch_office_bp)
app.register_blueprint(product_bp)
app.register_blueprint(price_bp)