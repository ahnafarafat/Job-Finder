from flask import Blueprint, render_template
from app.models import Job

public_bp = Blueprint('public', __name__)

@public_bp.route('/')
def home():
    jobs = Job.query.order_by(Job.posted_on.desc()).all()
    return render_template('public/home.html', jobs=jobs)