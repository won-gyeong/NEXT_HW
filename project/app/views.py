from django.shortcuts import render, redirect
from .models import Post
from django.utils import timezone
from datetime import timedelta

# Create your views here.

def home(request):
    posts = Post.objects.all()

    return render(request, 'home.html', {'posts': posts})


def new(request):
    if request.method == 'POST':
        new_post = Post.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            deadline = request.POST['deadline']
    )
        return redirect('detail', new_post.id)

    return render(request, 'new.html')

def detail(request, post_id):
    post = Post.objects.get(id = post_id)

    return render(request, 'detail.html', {'post': post})


def update(request, post_id):
    post = Post.objects.get(id = post_id)

    if request.method == 'POST':
        Post.objects.filter(id = post_id).update(
            title = request.POST['title'],
            content = request.POST['content'],
            deadline = request.POST['deadline']
        )
        return redirect('detail', post_id)
    
    return render(request, 'update.html', {'post': post})

def delete(request, post_id):
    post = Post.objects.get(id = post_id)
    post.delete()

    return redirect('home')