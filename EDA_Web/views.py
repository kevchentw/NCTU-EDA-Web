from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import HttpResponse as response

def home(request):
    if request.method == 'GET':
        return render(request, "home.html")
    elif request.method == 'POST':
        return response('')


def news(request):
    if request.method == 'GET':
        return render(request, "news.html")
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

