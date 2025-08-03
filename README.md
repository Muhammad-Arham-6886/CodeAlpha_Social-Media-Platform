# Social Media Platform

A simple and attractive social media platform built with Django.

## Features
- User profiles with profile pictures
- Posts with images and text
- Comments on posts
- Like/Unlike system
- Follow/Unfollow users
- Responsive design

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
```bash
# Windows
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

7. Visit `http://127.0.0.1:8000` in your browser

## Usage
- Register a new account or login
- Create posts with text and images
- Follow other users
- Like and comment on posts
- View user profiles
