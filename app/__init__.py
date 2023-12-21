from flask import Flask
from app.main import main_bp
from app.api.branch import branch_bp
from app.api.branch_office import branch_office_bp

app = Flask(__name__)
app.register_blueprint(main_bp)
app.register_blueprint(branch_bp)
app.register_blueprint(branch_office_bp)
