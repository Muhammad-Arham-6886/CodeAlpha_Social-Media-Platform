# Social Media Platform - Project Documentation

## Overview
SocialConnect is a simple yet attractive social media platform built with Django. It provides essential social media features in a clean, modern interface.

## Features

### Core Features
- **User Registration & Authentication**: Secure user signup, login, and logout
- **User Profiles**: Customizable profiles with bio and profile pictures
- **Posts**: Create posts with text and images
- **Comments**: Comment on posts with real-time interaction
- **Like System**: Like and unlike posts with AJAX functionality
- **Follow System**: Follow and unfollow other users
- **Search**: Search for users and posts
- **Responsive Design**: Mobile-friendly interface

### Technical Features
- **AJAX Like System**: Real-time like/unlike without page refresh
- **Image Upload & Processing**: Automatic image resizing and optimization
- **Pagination**: Efficient content loading for better performance
- **Form Validation**: Client and server-side form validation
- **User Signals**: Automatic profile creation for new users
- **Admin Interface**: Django admin for content management

## Project Structure

```
social_media_platform/
├── manage.py                   # Django management script
├── requirements.txt           # Python dependencies
├── README.md                 # Project overview
├── setup.py                  # Automated setup script
├── setup.bat                 # Windows setup script
├── run_server.bat           # Development server script
├── social_media/            # Main project directory
│   ├── __init__.py
│   ├── settings.py          # Django settings
│   ├── urls.py              # Main URL configuration
│   ├── wsgi.py              # WSGI configuration
│   └── asgi.py              # ASGI configuration
├── core/                    # Main application
│   ├── __init__.py
│   ├── models.py            # Database models
│   ├── views.py             # View functions
│   ├── urls.py              # App URL patterns
│   ├── forms.py             # Django forms
│   ├── admin.py             # Admin configuration
│   ├── apps.py              # App configuration
│   ├── signals.py           # Django signals
│   └── tests.py             # Unit tests
├── templates/core/          # HTML templates
│   ├── base.html            # Base template
│   ├── home.html            # Home page
│   ├── login.html           # Login page
│   ├── register.html        # Registration page
│   ├── logout.html          # Logout page
│   ├── profile.html         # Profile page
│   ├── profile_edit.html    # Profile editing
│   ├── post_create.html     # Post creation
│   ├── post_detail.html     # Post details
│   └── search.html          # Search results
├── static/core/             # Static files
│   ├── main.css             # Custom CSS
│   └── main.js              # JavaScript functionality
└── media/                   # User uploaded files
    ├── default.jpg          # Default profile picture
    ├── profile_pics/        # Profile pictures
    └── post_images/         # Post images
```

## Models

### User (Django's built-in)
- username, email, password, first_name, last_name

### Profile
- user (OneToOne with User)
- bio (TextField)
- profile_picture (ImageField)
- followers (ManyToMany with User)

### Post
- author (ForeignKey to User)
- content (TextField)
- image (ImageField, optional)
- date_posted (DateTimeField)
- likes (ManyToMany with User)

### Comment
- post (ForeignKey to Post)
- author (ForeignKey to User)
- content (TextField)
- date_posted (DateTimeField)

## Setup Instructions

### Automatic Setup (Recommended)
1. Run the setup script:
   ```bash
   # Windows
   setup.bat
   
   # Linux/Mac
   python setup.py
   ```

### Manual Setup
1. Create virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate virtual environment:
   ```bash
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
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

5. Create superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Start development server:
   ```bash
   python manage.py runserver
   ```

## Default Accounts
After running the setup script, you'll have:
- **Admin Account**: username: `admin`, password: `admin123`
- **Sample Users**: `john_doe`, `jane_smith`, `mike_wilson` (password: `password123`)

## Key Features Implementation

### Like System
- AJAX-powered like/unlike functionality
- Real-time UI updates without page refresh
- Heart animation for visual feedback

### Follow System
- Follow/unfollow users from their profiles
- Follower and following counts
- Permission checks to prevent self-following

### Image Handling
- Automatic image resizing for profile pictures (300x300)
- Support for various image formats
- Graceful fallback for missing images

### Search Functionality
- Search users by username or name
- Search posts by content or author
- Combined results display

### Responsive Design
- Bootstrap 5 for responsive layout
- Mobile-friendly navigation
- Optimized for various screen sizes

## Customization

### Styling
- Edit `static/core/main.css` for custom styles
- Bootstrap classes can be overridden
- CSS variables for easy color customization

### Features
- Add new models in `core/models.py`
- Create new views in `core/views.py`
- Add URL patterns in `core/urls.py`
- Create templates in `templates/core/`

### Settings
- Modify `social_media/settings.py` for configuration
- Update database settings for production
- Configure static files for deployment

## Security Considerations

### Current Security Features
- CSRF protection on all forms
- User authentication required for sensitive actions
- File upload validation
- XSS protection through template escaping

### Production Recommendations
- Change `SECRET_KEY` in settings
- Set `DEBUG = False`
- Configure proper database (PostgreSQL recommended)
- Use HTTPS in production
- Implement rate limiting
- Add user input sanitization

## Performance Optimizations

### Current Optimizations
- Database query optimization with select_related
- Image compression and resizing
- Pagination for post listings
- AJAX for like functionality

### Additional Recommendations
- Implement caching (Redis/Memcached)
- Use CDN for static files
- Database indexing for search queries
- Implement lazy loading for images

## Testing

### Running Tests
```bash
python manage.py test
```

### Test Coverage
- Model tests for all custom models
- View tests for all endpoints
- Form tests for validation
- Integration tests for user workflows

## Deployment

### Development
```bash
python manage.py runserver
```

### Production
1. Set up production database
2. Configure static files serving
3. Set up media files serving
4. Configure web server (Nginx/Apache)
5. Use application server (Gunicorn/uWSGI)

## Browser Support
- Chrome 70+
- Firefox 65+
- Safari 12+
- Edge 44+

## Contributing
1. Fork the repository
2. Create a feature branch
3. Make changes with tests
4. Submit a pull request

## License
This project is open source and available under the MIT License.

## Support
For issues and questions:
1. Check existing documentation
2. Search for similar issues
3. Create a new issue with detailed description

## Future Enhancements
- Real-time notifications
- Private messaging
- Story/Status features
- Advanced privacy settings
- API for mobile apps
- Social login (Google, Facebook)
- Content moderation tools
- Analytics dashboard
