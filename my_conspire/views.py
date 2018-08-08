from django.shortcuts import render, redirect

from my_conspire.forms import NewProfileForm, NewFeedForm, NewArticleForm
from my_conspire.models import Feed, Profile, Article


def welcome(request):
    title='welcome'
    return render(request, 'welcome.html', locals())

def all_feed(request):
    all_feed = Feed.objects.all()
    return render(request, 'index.html', locals())

def all_profiles(request, profile_id):
    profile = Profile.objects.get(user_id=profile_id)
    return render(request, 'profile.html', locals())


def new_profile(request):
    current_user = request.user

    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
            return redirect('feed')
    else:
        form = NewProfileForm()
    return render(request, 'new_profile.html', {"form": form})

def new_feed(request):
    current_user = request.user

    if request.method == 'POST':
        form = NewFeedForm(request.POST, request.FILES)
        if form.is_valid():
            feed = form.save(commit=False)
            feed.user = current_user
            feed.save()
            return redirect('feed')
    else:
        form = NewFeedForm()
    return render(request, 'new_feed.html', {"form": form})


def current_user_profile(request, profile_id):
    profile = Profile.objects.filter(user_id=profile_id).first()
    return render(request, 'current_user_profile.html', locals())


def all_articles(request):
    articles = Article.objects.all()
    return render(request, 'articles.html', locals())

def new_article(request):
    current_user = request.user

    if request.method == 'POST':
        form = NewArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = current_user
            article.save()
            return redirect('all-articles')
    else:
        form = NewArticleForm()
    return render(request, 'new_article.html', {"form": form})

def single_article(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'single_article.html', locals())