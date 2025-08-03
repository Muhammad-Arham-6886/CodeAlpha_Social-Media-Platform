from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='core/logout.html'), name='logout'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('profile-edit/', views.profile_edit, name='profile-edit'),
    path('post/new/', views.post_create, name='post-create'),
    path('post/<int:pk>/', views.post_detail, name='post-detail'),
    path('post/<int:pk>/like/', views.like_post, name='like-post'),
    path('follow/<str:username>/', views.follow_user, name='follow-user'),
    path('search/', views.search, name='search'),
]
