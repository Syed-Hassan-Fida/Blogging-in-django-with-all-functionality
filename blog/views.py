from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.


def index(request):
    # return HttpResponse("Home")
    return render(request, 'blog/home.html')


def about(request):
    # return HttpResponse("about")
    return render(request, 'blog/about.html')


def article(request):
    # return HttpResponse("about")
    articles = Article.objects.all().order_by("-date")
    # content = {
    #     "articles": articles
    # }
    
    return render(request, 'blog/articles.html', {'articles':articles})


# slug url function
def article_details(request, slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request, 'blog/details.html', {'article': article})

@login_required(login_url="/accounts/login/")
def create_view(request):
    if request.method == "POST":
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            instance.author = request.user
            instance.save()
            return redirect('blog:article')
    else:
        form = forms.CreateArticle()
    return render(request, 'blog/article_create.html', {'form': form})