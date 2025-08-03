from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Post, Profile, Comment
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, PostForm, CommentForm


def home(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 5)  # Show 5 posts per page
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    
    context = {
        'posts': posts,
        'title': 'Home'
    }
    return render(request, 'core/home.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'core/register.html', {'form': form})


@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=user)
    
    # Check if current user is following this profile user
    is_following = False
    if request.user.is_authenticated and request.user != user:
        is_following = user.profile.followers.filter(id=request.user.id).exists()
    
    context = {
        'profile_user': user,
        'posts': posts,
        'is_following': is_following,
        'followers_count': user.profile.followers.count(),
        'following_count': user.following.count(),
        'posts_count': posts.count(),
    }
    return render(request, 'core/profile.html', context)


@login_required
def profile_edit(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile', username=request.user.username)
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'core/profile_edit.html', context)


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Your post has been created!')
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'core/post_create.html', {'form': form})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    
    if request.method == 'POST':
        if request.user.is_authenticated:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                messages.success(request, 'Comment added successfully!')
                return redirect('post-detail', pk=post.pk)
        else:
            messages.error(request, 'You must be logged in to comment.')
    else:
        comment_form = CommentForm()
    
    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'core/post_detail.html', context)


@login_required
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    user = request.user
    
    if user in post.likes.all():
        post.likes.remove(user)
        liked = False
    else:
        post.likes.add(user)
        liked = True
    
    return JsonResponse({
        'liked': liked,
        'likes_count': post.total_likes()
    })


@login_required
def follow_user(request, username):
    user_to_follow = get_object_or_404(User, username=username)
    current_user = request.user
    
    if current_user != user_to_follow:
        if current_user in user_to_follow.profile.followers.all():
            user_to_follow.profile.followers.remove(current_user)
            following = False
            messages.success(request, f'You unfollowed {user_to_follow.username}')
        else:
            user_to_follow.profile.followers.add(current_user)
            following = True
            messages.success(request, f'You are now following {user_to_follow.username}')
    
    return redirect('profile', username=username)


def search(request):
    query = request.GET.get('q')
    users = []
    posts = []
    
    if query:
        users = User.objects.filter(
            Q(username__icontains=query) | 
            Q(first_name__icontains=query) | 
            Q(last_name__icontains=query)
        ).distinct()
        
        posts = Post.objects.filter(
            Q(content__icontains=query) | 
            Q(author__username__icontains=query)
        ).distinct()
    
    context = {
        'users': users,
        'posts': posts,
        'query': query,
    }
    return render(request, 'core/search.html', context)
