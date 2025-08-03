from django.contrib import admin
from .models import Profile, Post, Comment


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio']
    list_filter = ['user__date_joined']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'content', 'date_posted', 'total_likes']
    list_filter = ['date_posted', 'author']
    search_fields = ['content', 'author__username']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'post', 'content', 'date_posted']
    list_filter = ['date_posted', 'author']
    search_fields = ['content', 'author__username']
