# Django Task Manager

A portfolio-ready Task Manager web app built with Django and Bootstrap 5.

## Features
- User authentication (signup, login, logout)
- User-specific dashboards
- Create, read, update, delete (CRUD) tasks
- Mark tasks as completed/incomplete
- Responsive UI with Bootstrap 5
- Production settings (WhiteNoise for static files)

## Tech Stack
- Python 3.12, Django 5
- Bootstrap 5
- Gunicorn (for production)
- WhiteNoise (static files)

## Installation (Local)
1. Create venv and install:
   - `python -m venv .venv && .\.venv\Scripts\Activate.ps1`
   - `pip install -r requirements.txt`
2. Run migrations:
   - `python manage.py migrate`
3. Start server:
   - `python manage.py runserver`
4. Visit: http://127.0.0.1:8000

## Live Demo
- URL: REPLACE_WITH_DEPLOYED_URL

## Screenshots
- `screenshots/home.png`
- `screenshots/dashboard.png`

## How to Use
- Sign up or login
- Create tasks from "New Task"
- Toggle complete/incomplete from dashboard
- Edit or delete tasks as needed

## License
MIT
