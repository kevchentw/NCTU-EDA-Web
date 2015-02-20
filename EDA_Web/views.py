# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import HttpResponse as response
from news.models import NewsModel
from EDA_Web.service import Service
import EDA_Web.ui as ui


def home(request):
    if request.method == 'GET':
        d = {}
        d['news_list_1'] = NewsModel.objects.filter(top__exact=True).order_by('-modified_time')[:3]
        d['news_list_0'] = NewsModel.objects.filter(top__exact=False).order_by('-modified_time')[:6]
        return render(request, "home.html", d)
    elif request.method == 'POST':
        return response('')


def news(request):
    if request.method == 'GET':
        d = {}
        d['news_list_1'] = NewsModel.objects.filter(top__exact=True).order_by('-modified_time')
        d['news_list_0'] = NewsModel.objects.filter(top__exact=False).order_by('-modified_time')
        return render(request, "news.html", d)
    elif request.method == 'POST':
        req = request.POST.get('req', 'err')
        title = request.POST.get('title', 'Untitled')
        content = request.POST.get('content', 'No content')
        author = request.POST.get('author', 'Anonymous')
        classification = request.POST.get('classification', '未分類')
        top = request.POST.get('top', False)
        if top:
            top = True
        if req == 'add':
            err, nid = Service.News.add_news(title, top, content, author, classification)
            d = {}
            d['news_list_1'] = NewsModel.objects.filter(top__exact=True).order_by('-modified_time')
            d['news_list_0'] = NewsModel.objects.filter(top__exact=False).order_by('-modified_time')
            d['message'] = ui.message("新增成功", "編號:" + str(nid), "blue")
            return render(request, "news.html", d)
        elif req == 'del':
            nid = request.POST['nid']
            err, nid = Service.News.del_news(nid)
            if err:
                return response(err)
            return response('S')
        elif req == 'mod':
            err, nid = Service.News.mod_news(title, top, content, author, classification)
            if err:
                return response(err)
            return response(str(nid))

        return response('undefined')


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


def kcw_research(request):
    if request.method == 'GET':
        return render(request, "kcw_research.html")
    elif request.method == 'POST':
        return response('')


def tyho(request):
    if request.method == 'GET':
        return render(request, "tyho.html")
    elif request.method == 'POST':
        return response('')


def tyho_research(request):
    if request.method == 'GET':
        return render(request, "tyho_research.html")
    elif request.method == 'POST':
        return response('')


def ylli(request):
    if request.method == 'GET':
        return render(request, "ylli.html")
    elif request.method == 'POST':
        return response('')


def ylli_research(request):
    if request.method == 'GET':
        return render(request, "ylli_research.html")
    elif request.method == 'POST':
        return response('')


def logout(request):
    logout(request)


def reset(request):
    NewsModel.objects.all().delete()