from flask import Blueprint, render_template
from app.models import Job

public_bp = Blueprint('public', __name__)

@public_bp.route('/jobs')
def job_list():
    jobs = Job.query.all()
    return render_template('public/job_list.html', jobs=jobs)