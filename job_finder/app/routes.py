from flask import Blueprint, render_template
from app.models import Job

admin_bp = Blueprint('admin', __name__)

@admin_bp.route("/")
def admin_dashboard():
    jobs = Job.query.all()
    return render_template("admin/dashboard.html", jobs=jobs)