from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login


def home(request):
    return render(request, "home.html")


def news(request):
    return render(request, "news.html")


def feeds(request):
    return render(request, "feeds.html")


def members(request):
    return render(request, "members.html")


def about(request):
    return render(request, "about.html")


def downloads(request):
    return render(request, "downloads.html")


def achievement(request):
    return render(request, "achievement.html")


def activity(request):
    return render(request, "activity.html")


def contact(request):
    return render(request, "contact.html")

