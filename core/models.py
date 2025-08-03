from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
import os


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(default='default.svg', upload_to='profile_pics')
    followers = models.ManyToManyField(User, related_name='following', blank=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        # Only resize if the file exists and is a real image
        if self.profile_picture and hasattr(self.profile_picture, 'path'):
            try:
                if os.path.exists(self.profile_picture.path):
                    img = Image.open(self.profile_picture.path)
                    if img.height > 300 or img.width > 300:
                        output_size = (300, 300)
                        img.thumbnail(output_size)
                        img.save(self.profile_picture.path)
            except Exception:
                # If image processing fails, just continue
                pass
    
    def get_absolute_url(self):
        return reverse('profile', kwargs={'username': self.user.username})


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images', blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    
    class Meta:
        ordering = ['-date_posted']
    
    def __str__(self):
        return f'Post by {self.author.username} on {self.date_posted.strftime("%Y-%m-%d")}'
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    date_posted = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['date_posted']
    
    def __str__(self):
        return f'Comment by {self.author.username} on {self.post}'
