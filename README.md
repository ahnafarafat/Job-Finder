# 🧠 JobFinder — Flask Admin Dashboard for Job Management

A backend-focused web application built with Flask that powers the **Admin Dashboard** for a Job Finder platform. This system enables administrators to securely log in, manage job listings, and perform CRUD operations — all from a clean, structured dashboard interface.

---

## 📍 Project Status

🚧 **Currently in the Deployment Stage.**  
✅ Core features (admin login, job creation/deletion/dashboard) are fully functional.  
🐞 Bug-fixing and server configuration are in progress for production deployment (Render).

---

## 🎯 Key Features

- 🔐 Secure Admin Login System (with password hashing)
- ➕ Add New Job Postings
- 🗑️ Delete Existing Job Listings
- 📋 Dashboard View of All Jobs
- 🔒 Login-protected Routes
- ⚙️ Modular Flask Application Structure
- 🌐 Ready for Deployment with Gunicorn + WSGI

---

## 🛠 Tech Stack

| Layer          | Technology                           |
|----------------|--------------------------------------|
| Backend        | Python 3, Flask                      |
| Database       | SQLite (local), PostgreSQL (prod)    |
| ORM            | SQLAlchemy                           |
| Auth           | Flask-Login, Werkzeug                |
| Templating     | Jinja2                               |
| Forms          | Flask-WTF                            |
| Deployment     | Render, Gunicorn, WSGI               |

---

## 📂 Project Structure

job_finder/
├── app/
│ ├── init.py # App factory
│ ├── models.py # SQLAlchemy models
│ ├── forms.py # Flask-WTF forms
│ ├── auth.py # Login/logout logic
│ ├── extensions.py # DB & login manager
│ ├── routes/
│ │ └── routes.py # Admin routes
│ └── templates/ # HTML templates
├── config.py # App configuration
├── run.py # Local entry point
├── wsgi.py # WSGI entry point for gunicorn
├── add_admin.py # CLI script to add admin
├── create_user.py # (Optional) additional user setup
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── runtime.txt # Python version pinning

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/jobfinder-admin.git
cd jobfinder-admin

### 2. Set Up Virtual Environment

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

### 3. Initialize Database

flask db init
flask db migrate
flask db upgrade

### 4. Add Admin User

python add_admin.py

### 5. Run the App (Locally)

python run.py

# 🌍 Deployment (Render / Production)

gunicorn wsgi:app

✅ Completed Milestones
 Admin login/logout with session management

 Job model & job form setup

 Admin dashboard with job list view

 Job creation & deletion

 App factory pattern with Blueprints

 CLI tool to add admin user

 Render deployment configuration (wsgi, gunicorn, runtime.txt)

🔜 Coming Soon
 Frontend job seeker interface

 API endpoints for public job listings

 Job search, filters, and pagination

 Resume upload and contact system

 Admin role management and access control

👨‍💻 About the Developer
Ahnaf Arafat
💼 Aspiring Backend Developer | Python & Flask & Django
🔗 LinkedIn:  | 🌐 Portfolio

This project is a demonstration of clean backend architecture, deployment-readiness, and practical admin tools — perfect for real-world job board use cases.