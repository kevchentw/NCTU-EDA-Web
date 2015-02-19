from news.models import NewsModel


class Service:
    pass


class NewsService:
    def __init__(self):
        self.newsdb = NewsModel.objects

    def get_news_all(self):
        nl = self.newsdb.all()
        nl = sorted(nl, key=lambda news: news.modified_time)
        return (None, nl)

    def get_news_by_id(self, nid):
        cur = self.newsdb.raw('SELECT * FROM "news_newsmodel" '
                              'WHERE "news_newsmodel"."nid" = %s', [nid])
        if len(list(cur)) > 1:
            return ('Eduplicate', None)
        elif len(list(cur)) == 0:
            return ('Enoexist', None)
        else:
            reutrn('EDB', None)
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

