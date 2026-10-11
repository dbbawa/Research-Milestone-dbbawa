# Research-Milestone-dbbawa

Django

Sample app for the Estate Property Management capstone project (Gitty_up), built with Django to evaluate it as our tech stack.

## What it does
- Employee login/logout with password checking and sessions (Django's built-in auth)
- Portfolio dashboard listing properties from the database, with photos
- Add, edit, and delete properties (including image upload)
- Property detail page with bedrooms, bathrooms, rent, and units
- Add units to a property (linked to it with a foreign key)

## Tech
Python 3.13, Django 6.1, SQLite, Pillow for images

## How to run
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Then open http://127.0.0.1:8000 and sign in.

## My notes on Django
- **Pros:** login, sessions, and the admin panel came built in.
- **Cons:** pages are server-rendered templates.
- **Setup difficulty:** not too difficult.
- **Would I recommend it for our project?** yes
