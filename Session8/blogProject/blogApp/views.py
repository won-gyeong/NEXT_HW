from django.shortcuts import render, redirect
from .models import Article
from datetime import datetime


# Create your views here.

def new(request):


    if request.method == 'POST':

        new_article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            category = request.POST['category'],
            # date = datetime.now()
        )

        return redirect('list')


    return render(request, 'new.html')


def home(request):
    articles = Article.objects.all()
    categories = []
    for article in articles:
        if article.category not in categories:
            categories.append(article.category)

    return render(request, 'home.html', {'categories':categories})


def list(request):
    articles = Article.objects.all().order_by("-pub_date")
    return render(request, 'list.html', {'articles':articles})


def category(request, category):
    articles = Article.objects.filter(category = category)
    count = articles.count()
    print(articles, '==확인==')
    return render(request, 'category.html',  {'articles':articles, 'count':count})


def detail(request, article_id):
    article = Article.objects.get(id = article_id)
    return render(request, 'detail.html', {'article':article})