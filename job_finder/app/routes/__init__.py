from app.routes.admin import admin_bp
from app.routes.public import public_bp

def register_blueprints(app):
    app.register_blueprint(admin_bp)
    app.register_blueprint(public_bp)