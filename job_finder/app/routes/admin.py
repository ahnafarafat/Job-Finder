from flask import Blueprint, render_template, redirect, url_for, request, session
from app.models import Job
from app import db

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'admin':
            session['admin_logged_in'] = True
            return redirect(url_for('admin.dashboard'))
    return render_template('admin/login.html')

@admin_bp.route('/dashboard')
def dashboard():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin.login'))
    jobs = Job.query.all()
    return render_template('admin/dashboard.html', jobs=jobs)

@admin_bp.route('/add-job', methods=['GET', 'POST'])
def add_job():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin.login'))
    if request.method == 'POST':
        job = Job(
            title=request.form['title'],
            company=request.form['company'],
            location=request.form['location'],
            description=request.form['description']
        )
        db.session.add(job)
        db.session.commit()
        return redirect(url_for('admin.dashboard'))
    return render_template('admin/add_job.html')

@admin_bp.route('/delete-job/<int:job_id>')
def delete_job(job_id):
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin.login'))
    job = Job.query.get_or_404(job_id)
    db.session.delete(job)
    db.session.commit()
    return redirect(url_for('admin.dashboard'))

@admin_bp.route('/logout')
def logout():
    session.pop("admin_logged_in", None)
    return redirect(url_for('admin.login'))


