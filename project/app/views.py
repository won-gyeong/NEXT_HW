from django.shortcuts import render, redirect
from .models import Post, Comment, Recomment
from django.utils import timezone
from datetime import timedelta

# Create your views here.

def home(request):
    posts = Post.objects.all().order_by("deadline")

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
   post = Post.objects.get(id=post_id)
   print(post)
   if request.method == 'POST':
       content = request.POST['content']
       Comment.objects.create(
           post = post,
           content = content
       )
       return redirect('detail', post_id)

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

def delete_comment(request, post_id, comment_id):
    comment = Comment.objects.get(id = comment_id)
    comment.delete()
    return redirect('detail', post_id)


def recomment(request, post_id, comment_id):
    comment = Comment.objects.get(id = comment_id)
    if request.method == "POST":
        recomments = Recomment.objects.create(
            comment = comment,
            content = request.POST['content'],
        )
        return redirect('detail', post_id)

def delete_recomment(request, post_id, recomment_id):
    recomment = Recomment.objects.get(id = recomment_id)
    recomment.delete()
    return redirect('detail', post_id)
