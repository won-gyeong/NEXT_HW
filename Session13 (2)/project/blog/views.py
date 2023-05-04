from django.shortcuts import render, redirect
from .models import Post, Comment, Recomment
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login(request):
   if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']

       user = auth.authenticate(username=username, password=password)

       if user is not None:
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect(request.GET.get('next', '/blog/'))
       error = "아이디 또는 비밀번호가 틀립니다"
       return render(request, 'registration/login.html', {"error":error})

   return render(request, 'registration/login.html')


def logout(request):
   auth.logout(request)
   return redirect('blog:home')

def signup(request):
   if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']
       
       exist_user = User.objects.filter(username=username)

       if exist_user:
           error = "이미 존재하는 아이디입니다"
           return render(request, 'registration/signup.html', {"error": error})
       
       new_user = User.objects.create_user(username=username, password=password)
       auth.login(request, new_user, backend='django.contrib.auth.backends.ModelBackend')
       return redirect('blog:home')

   return render(request, 'registration/signup.html')

def home(request):
    posts = Post.objects.all().order_by("deadline")

    return render(request, 'blog/home.html', {'posts': posts})

@login_required(login_url="/registration/login/")
def new(request):
    if request.method == 'POST':
        new_post = Post.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            deadline = request.POST['deadline'],
            author=request.user
    )
        return redirect('blog:detail', new_post.id)

    return render(request, 'blog/new.html')

@login_required(login_url="/registrations/login/")
def detail(request, post_id):
   post = Post.objects.get(id=post_id)
   print(post)
   if request.method == 'POST':
       content = request.POST['content']
       Comment.objects.create(
           post = post,
           content = content,
           author = request.user
       )
       return redirect('blog:detail', post_id)

   return render(request, 'blog/detail.html', {'post': post})


def update(request, post_id):
    post = Post.objects.get(id = post_id)

    if request.method == 'POST':
        Post.objects.filter(id = post_id).update(
            title = request.POST['title'],
            content = request.POST['content'],
            deadline = request.POST['deadline']
        )
        return redirect('blog:detail', post_id)
    
    return render(request, 'blog/update.html', {'post': post})

def delete(request, post_id):
    post = Post.objects.get(id = post_id)
    post.delete()

    return redirect('blog:home')

def delete_comment(request, post_id, comment_id):
    comment = Comment.objects.get(id = comment_id)
    comment.delete()
    return redirect('blog:detail', post_id)


def recomment(request, post_id, comment_id):
    comment = Comment.objects.get(id = comment_id)
    if request.method == "POST":
        recomments = Recomment.objects.create(
            comment = comment,
            content = request.POST['content'],
        )
        return redirect('blog:detail', post_id)

def delete_recomment(request, post_id, recomment_id):
    recomment = Recomment.objects.get(id = recomment_id)
    recomment.delete()
    return redirect('blog:detail', post_id)
