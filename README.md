# JobFinder — Flask Admin Dashboard for Job Management

A backend-focused web application built with **Flask** that powers the **Admin Dashboard** for a Job Finder platform.  
This system enables administrators to securely log in, manage job listings, and perform CRUD operations — all from a clean, structured dashboard interface.

---

## Project Status

**Currently in the Deployment Stage**  
- Core features are fully functional (admin login, job creation, job dashboard)  
- Bug-fixing and server configuration are in progress for production deployment on **Render**

---

## Key Features

- Secure Admin Login System (password hashing with Flask-Login)
- Add New Job Postings
- Dashboard View of All Jobs
- Login-protected Routes
- Modular Flask Application Structure using App Factory & Blueprints
- Ready for Deployment (Gunicorn + WSGI + Render)

---

## Tech Stack

| Layer      | Technology                        |
| ---------- | --------------------------------- |
| Backend    | Python 3, Flask                   |
| Database   | SQLite (local), PostgreSQL (prod) |
| ORM        | SQLAlchemy                        |
| Auth       | Flask-Login, Werkzeug             |
| Forms      | Flask-WTF                         |
| Templating | Jinja2                            |
| Deployment | Render, Gunicorn, WSGI            |

---

## Project Structure

```

job\_finder/
├── app/
│   ├── **init**.py          # App factory
│   ├── models.py            # SQLAlchemy models
│   ├── forms.py             # Flask-WTF forms
│   ├── auth.py              # Login/logout logic
│   ├── extensions.py        # DB & login manager
│   ├── routes/
│   │   └── routes.py        # Admin routes
│   └── templates/           # HTML templates
├── config.py                # App configuration
├── run.py                   # Local entry point
├── wsgi.py                  # WSGI entry point for gunicorn
├── add\_admin.py             # CLI tool to add admin
├── create\_user.py           # Optional user creation script
├── requirements.txt         # Python dependencies
├── runtime.txt              # Python version pinning
└── README.md                # Project documentation

````

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/itsahnafarafat/Website.git
cd Website
````

### 2. Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Initialize the Database

```bash
flask db init
flask db migrate
flask db upgrade
```

### 4. Add an Admin User

```bash
python add_admin.py
```

### 5. Run the App Locally

```bash
python run.py
```

---

## Deployment (Render / Production)

```bash
gunicorn wsgi:app
```

Ensure `runtime.txt`, `requirements.txt`, and `wsgi.py` are included for a successful deployment to Render or similar platforms.

---

## Completed Milestones

* Admin login/logout with session management
* Job model & job form setup
* Admin dashboard with job list view
* Job creation & deletion
* App factory pattern with Blueprints
* CLI tool to add admin user
* Render deployment configuration (WSGI, Gunicorn, runtime.txt)

---

## Coming Soon

* Frontend job seeker interface
* Public API endpoints for job listings
* Resume upload and contact form system
* Job search, filters, and pagination
* Admin role management and access control

```

```
## About the Developer

**Ahnaf Arafat**
*Aspiring Backend Developer | Python • Flask • Django*
🔗 [LinkedIn Profile](https://www.linkedin.com/in/ahnaf-arafat-30189a357/)

---

## Project Vision

This project is a demonstration of:

* Clean backend architecture with Flask
* Deployment-ready design using Gunicorn & WSGI
* Practical admin workflows for real-world job boards

It’s designed to reflect real job experience and backend competency for production-focused applications.

---
