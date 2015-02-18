from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import HttpResponse as response
from news.models import NewsModel

def home(request):
    if request.method == 'GET':
        return render(request, "home.html")
    elif request.method == 'POST':
        return response('')


def news(request):
    if request.method == 'GET':
        news_list = NewsModel.objects.all()
        d = {}
        nl = []
        ntl = []
        for n in news_list:
            if n.top:
                ntl.append({'title' : n.title,
                    'content' : n.content,
                    'author' : n.author,
                    'created_time' : n.created_time,
                    'modified_time' : n.modified_time,
                    'classification' : n.classification})
            else:
                nl.append({'title' : n.title,
                    'content' : n.content,
                    'author' : n.author,
                    'created_time' : n.created_time,
                    'modified_time' : n.modified_time,
                    'classification' : n.classification})

        d['news_list_0'] = nl
        d['news_list_1'] = ntl
        return render(request, "news.html",d)
    elif request.method == 'POST':
        return response('')


def feeds(request):
    if request.method == 'GET':
        return render(request, "feeds.html")
    elif request.method == 'POST':
        return response('')


def members(request):
    if request.method == 'GET':
        return render(request, "members.html")
    elif request.method == 'POST':
        return response('')


def about(request):
    if request.method == 'GET':
        return render(request, "about.html")
    elif request.method == 'POST':
        return response('')


def downloads(request):
    if request.method == 'GET':
        return render(request, "downloads.html")
    elif request.method == 'POST':
        return response('')


def achievement(request):
    if request.method == 'GET':
        return render(request, "achievement.html")
    elif request.method == 'POST':
        return response('')


def activity(request):
    if request.method == 'GET':
        return render(request, "activity.html")
    elif request.method == 'POST':
        return response('')


def contact(request):
    if request.method == 'GET':
        return render(request, "contact.html")
    elif request.method == 'POST':
        return response('')


def kcw(request):
    if request.method == 'GET':
        return render(request, "kcw.html")
    elif request.method == 'POST':
        return response('')


def tyho(request):
    if request.method == 'GET':
        return render(request, "tyho.html")
    elif request.method == 'POST':
        return response('')


def ylli(request):
    if request.method == 'GET':
        return render(request, "ylli.html")
    elif request.method == 'POST':
        return response('')