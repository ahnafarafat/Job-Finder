from app import create_app
from app.extensions import db
from app.models import User
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    existing_user = User.query.filter_by(username='admin').first()
    if not existing_user:
        hashed_password = generate_password_hash('admin123')
        new_user = User(username='admin', password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        print("Admin user created.")
    else:
        print("Admin user already exists.")
