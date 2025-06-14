from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Create database instance (globally)
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # App Configuration
    app.config['SECRET_KEY'] = 'your-secret-key'  # Change this in production!
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobs.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    from app.routes.admin import admin_bp
    app.register_blueprint(admin_bp, url_prefix='/admin')

    return app







