from app.main import main_bp

@main_bp.route("/")
def index():
    return "<h1>iBarber Store!</h1>"