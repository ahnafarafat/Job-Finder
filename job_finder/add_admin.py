from app import create_app
from app.models import db, User

app = create_app()

with app.app_context():
    user = User.query.filter_by(username='admin').first()
    print("Admin user added successfully!")



