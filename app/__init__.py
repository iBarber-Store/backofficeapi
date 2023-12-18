from flask import Flask
from app.main import main_bp
from app.branch import branch_bp

app = Flask(__name__)
app.register_blueprint(main_bp)
app.register_blueprint(branch_bp)
