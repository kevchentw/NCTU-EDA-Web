# -*- coding: utf-8 -*-
from news.models import NewsModel
from downloads.models import DownloadsModel
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
import os


class Service:
    pass


class NewsService:
    def __init__(self):
        self.newsdb = NewsModel.objects

    def get_news_all(self):
        nl = self.newsdb.all()
        nl = sorted(nl, key=lambda news: news.modified_time, reverse=True)
        return (None, nl)

    def get_news_all_dict(self, d={"init": "get_news_all_dict"}, top_num=10000000, non_top_num=10000000):
        err, news_list = self.get_news_all()
        nl = []
        ntl = []
        for n in news_list:
            if n.top:
                if top_num > 0:
                    ntl.append(n)
                top_num -= 1
            else:
                if non_top_num > 0:
                    nl.append(n)
                non_top_num -= 1
        d['news_list_0'] = nl
        d['news_list_1'] = ntl
        return (None, d)

    def get_news_by_id(self, nid):
        cur = self.newsdb.raw('SELECT * FROM "news_newsmodel" '
                              'WHERE "news_newsmodel"."nid" = %s', [nid])
        if len(list(cur)) > 1:
            return ('Eduplicate', None)
        elif len(list(cur)) <= 0:
            return ('Enoexist', None)
        return (None, cur[0])

    def add_news(self, title, top, content, author, classification):
        n = self.newsdb.create(title=title, top=top, content=content,
                               author=author, classification=classification)
        return (None, n.nid)

    def del_news(self, nid):
        err, n = self.get_news_by_id(nid)
        if err:
            return (err, None)
        n.delete()
        return (None, nid)

    def mod_news(self, nid, title, top, content, author, classification):
        err, n = self.get_news_by_id(nid)
        if err:
            return (err, None)
        n.title = title
        n.top = top
        n.content = content
        n.author = author
        n.classification = classification
        n.save()
        return (None, nid)


def log(s):
    f = open('log', 'a+')
    f.write(str(s) + '\n')
    f.close()


class DownloadsService:
    def __init__(self):
        self.downloadsdb = DownloadsModel.objects

    def add_downloads(self, filename, description, classification, uploader, attach_file):
        try:
            self.downloadsdb.get(filename__exact=filename)
            return ('Eexist', None)
        except ObjectDoesNotExist:
            pass

        d = self.downloadsdb.create(filename=filename, description=description, classification=classification,
                                    uploader=uploader)
        path = settings.DOCUMENT_ROOT + '/' + filename
        f = open(path, 'wb+')
        for chunk in attach_file.chunks():
            f.write(chunk)
        f.close()
        return (None, d.did)

    def del_downloads(self, did):
        log(did)
        try:
            d = self.downloadsdb.get(did__exact=did)
            path = settings.DOCUMENT_ROOT + '/' + d.filename
            try:
                os.remove(path)
            except:
                pass
            d.delete()
            return (None, did)
        except ObjectDoesNotExist:
            return ('Enoexist', None)

    def mod_downloads(self, did, description, uploader, classification, attach_file):
        try:
            d = self.downloadsdb.get(did__exact=did)
        except ObjectDoesNotExist:
            return ('Enoexist', None)
        log(description)
        d.description = description
        d.uploader = uploader
        d.classification = classification
        d.save()
        if attach_file:
            path = settings.DOCUMENT_ROOT + '/' + d.filename
            os.remove(path)
            filename = str(attach_file)
            d.filename = filename
            d.save()
            path = settings.DOCUMENT_ROOT + '/' + filename
            log('save')
            log(type(attach_file))
            f = open(path, 'wb+')
            for chunk in attach_file.chunks():
                f.write(chunk)
            f.close()
        return (None, did)
