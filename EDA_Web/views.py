# -*- coding: utf-8 -*-
import math
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login as auth_login, authenticate
from django.shortcuts import HttpResponse as response
from django.core.exceptions import ObjectDoesNotExist
from news.models import NewsModel
from downloads.models import DownloadsModel
from EDA_Web.service import Service


def log(s):
    f = open('log', 'a')
    f.write(str(s)+'\n')
    f.close()
    return


def home(request):
    if request.method == 'GET':
        d = {}
        d['news_list_1'] = NewsModel.objects.filter(top__exact=True).order_by('-modified_time')[:3]
        tmp = max(6-len(d['news_list_1']), 4)
        print(tmp)
        d['news_list_0'] = NewsModel.objects.filter(top__exact=False).order_by('-modified_time')[:tmp]
        return render(request, "home.html", d)
    elif request.method == 'POST':
        return response('')


def news(request):
    if request.method == 'GET':
        page = int(request.GET.get('page', '1'))
        d = {}
        d['news_list_1'] = NewsModel.objects.filter(top__exact=True).order_by('-modified_time')
        nl = NewsModel.objects.filter(top__exact=False).order_by('-modified_time')
        try:
            d['news_list_0'] = nl[(page-1)*7: min(len(nl)-1, (page-1)*7+7)]
        except:
            d['news_list_0'] = []
        for n in d['news_list_0']:
            n.content = n.content.split('\n')[0][:15]
        for n in d['news_list_1']:
            n.content = n.content.split('\n')[0][:15]
        d['page'] = page
        d['max_page'] = range(1, int(math.ceil(len(nl)/7)+1))
        d['_max_page'] = math.ceil(len(nl)/7)
        d['pre_page'] = page - 1 if page != 1 else page
        d['nxt_page'] = page + 1 if page != d['_max_page'] else page
        return render(request, "news.html", d)
    elif request.method == 'POST':
        req = request.POST.get('req', 'err')
        title = request.POST.get('title', 'Untitled')
        content = request.POST.get('content', 'No content')
        author = request.POST.get('author', 'Anonymous')
        classification = request.POST.get('classification', '未分類')
        top = True if request.POST.get('top', False) == '1' else False
        if top:
            top = True
        if req == 'add':
            author = request.user.username
            err, nid = Service.News.add_news(title, top, content, author, classification)
            return response(str(nid))
        elif req == 'del':
            try:
                nid = request.POST.get('nid', '-1')
                if nid.isdigit():
                    nid = int(nid)
                    NewsModel.objects.get(nid__exact=nid).delete()
                else:
                    return response('noexist')
            except ObjectDoesNotExist:
                return response('noexist')
            return response('S')
        elif req == 'mod':
            nid = request.POST.get('nid', '-1')
            err, nid = Service.News.mod_news(nid, title, top, content, author, classification)
            if err:
                return response(err)
            return response(str(nid))

        return response('undefined')


def news_detail(request, nid):
    if request.method == "GET":
        if nid.isdigit():
            nid = int(nid)
            d = {}
            d['news'] = NewsModel.objects.get(nid__exact=nid)
            return render(request, "news_detail.html", d)
        else:
            return response('noexist')


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

def members_student(request):
    if request.method == 'GET':
        return render(request, "members_student.html")
    elif request.method == 'POST':
        return response('')

def about(request):
    if request.method == 'GET':
        return render(request, "about.html")
    elif request.method == 'POST':
        return response('')


def downloads(request):
    if request.method == 'GET':
        did = request.GET.get('did', '-1')
        d = {}
        d['downloads0'] = DownloadsModel.objects.filter(classification__exact='論文').order_by('-created_time')
        d['downloads1'] = DownloadsModel.objects.filter(classification__exact='文件').order_by('-created_time')
        try:
            d['modify'] = DownloadsModel.objects.get(did__exact=did)
        except ObjectDoesNotExist:
            d['modify'] = None
        log(d['modify'])
        log(did)
        return render(request, "downloads.html", d)
    elif request.method == 'POST':
        req = request.POST.get('req', '')
        if req == 'add':
            description = request.POST.get('description', '')
            classification = request.POST.get('classification', '')
            uploader = request.POST.get('uploader', '')
            filename = str(request.FILES['attach_file'])
            err, did = Service.Downloads.add_downloads(filename, description, classification, uploader,
                                                       request.FILES['attach_file'])
            if err:
                return response(err)
            return response(str(did))
        elif req == 'del':
            did = request.POST.get('did','-1')
            err, did = Service.Downloads.del_downloads(did)
            if err:
                return response(err)
            return response(str(did))
        elif req == 'mod':
            did = request.POST.get('did', '-1')
            description = request.POST.get('description', '')
            uploader = request.POST.get('uploader', '')
            classification = request.POST.get('classification', '')
            log('into')
            log(description)
            err, did = Service.Downloads.mod_downloads(did, description, uploader, classification, 
                    request.FILES.get('attach_file')) 
            if err:
                return response(err)
            return response(str(did))
        return response('undefined')


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
        return redirect('http://eda.cs.nctu.edu.tw')
        return render(request, "ylli_research.html")
    elif request.method == 'POST':
        return response('')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        if request.user.is_authenticated():
            return response('Ealready login')
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return redirect("/")
            else:
                return response('Edisabled account')
        else:
            return response('Einvalid login')


def reset(request):
    '''n = NewsModel.objects.all()
    for nn in n:
        if nn.nid != 15:
            nn.delete()
    '''
