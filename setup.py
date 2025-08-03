#!/usr/bin/env python
"""
Setup script for Social Media Platform
This script helps set up the Django application and create initial data
"""

import os
import sys
import django
from django.core.management import execute_from_command_line

def setup_django():
    """Set up Django environment"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social_media.settings')
    django.setup()

def create_migrations():
    """Create database migrations"""
    print("Creating migrations...")
    execute_from_command_line(['manage.py', 'makemigrations'])
    print("✓ Migrations created")

def migrate_database():
    """Apply database migrations"""
    print("Applying migrations...")
    execute_from_command_line(['manage.py', 'migrate'])
    print("✓ Database migrated")

def create_superuser():
    """Create superuser if it doesn't exist"""
    from django.contrib.auth.models import User
    
    if not User.objects.filter(is_superuser=True).exists():
        print("Creating superuser...")
        try:
            User.objects.create_superuser(
                username='admin',
                email='admin@socialconnect.com',
                password='admin123'
            )
            print("✓ Superuser created (username: admin, password: admin123)")
        except Exception as e:
            print(f"✗ Error creating superuser: {e}")
    else:
        print("✓ Superuser already exists")

def create_sample_data():
    """Create sample posts and users"""
    from django.contrib.auth.models import User
    from core.models import Post, Profile
    
    # Create sample users
    sample_users = [
        {'username': 'john_doe', 'email': 'john@example.com', 'first_name': 'John', 'last_name': 'Doe'},
        {'username': 'jane_smith', 'email': 'jane@example.com', 'first_name': 'Jane', 'last_name': 'Smith'},
        {'username': 'mike_wilson', 'email': 'mike@example.com', 'first_name': 'Mike', 'last_name': 'Wilson'},
    ]
    
    print("Creating sample users...")
    for user_data in sample_users:
        user, created = User.objects.get_or_create(
            username=user_data['username'],
            defaults={
                'email': user_data['email'],
                'first_name': user_data['first_name'],
                'last_name': user_data['last_name']
            }
        )
        if created:
            user.set_password('password123')
            user.save()
            # Update profile bio
            user.profile.bio = f"Hello! I'm {user.first_name}. Welcome to my profile!"
            user.profile.save()
            print(f"✓ Created user: {user.username}")
    
    # Create sample posts
    sample_posts = [
        {
            'author': 'john_doe',
            'content': 'Welcome to SocialConnect! This is my first post. Excited to connect with everyone! 🎉'
        },
        {
            'author': 'jane_smith',
            'content': 'Beautiful sunset today! Nature never fails to amaze me. What\'s your favorite time of day? 🌅'
        },
        {
            'author': 'mike_wilson',
            'content': 'Just finished reading an amazing book about technology. Any book recommendations for a tech enthusiast? 📚'
        },
        {
            'author': 'john_doe',
            'content': 'Coffee and coding - the perfect combination for a productive morning! ☕💻'
        },
        {
            'author': 'jane_smith',
            'content': 'Exploring new places and meeting new people. Travel broadens the mind! ✈️🗺️'
        },
    ]
    
    print("Creating sample posts...")
    for post_data in sample_posts:
        try:
            author = User.objects.get(username=post_data['author'])
            post, created = Post.objects.get_or_create(
                author=author,
                content=post_data['content']
            )
            if created:
                print(f"✓ Created post by {author.username}")
        except User.DoesNotExist:
            print(f"✗ User {post_data['author']} not found")

def main():
    """Main setup function"""
    print("🚀 Setting up Social Media Platform...")
    print("=" * 50)
    
    # Set up Django
    setup_django()
    
    # Create migrations and migrate
    create_migrations()
    migrate_database()
    
    # Create superuser
    create_superuser()
    
    # Create sample data
    create_sample_data()
    
    print("\n" + "=" * 50)
    print("✅ Setup complete!")
    print("\nNext steps:")
    print("1. Run 'python manage.py runserver' to start the development server")
    print("2. Visit http://127.0.0.1:8000 in your browser")
    print("3. Login with username 'admin' and password 'admin123' (or create a new account)")
    print("4. Explore the platform and create your first post!")
    print("\nEnjoy using SocialConnect! 🎉")

if __name__ == '__main__':
    main()
