from django.db import models
from django.utils import timezone
import datetime


class NewsModel(models.Model):
    nid = models.AutoField(primary_key=True)
    top = models.BooleanField(default=False)
    created_time = models.DateTimeField(editable=False)
    modified_time = models.DateTimeField()
    title = models.TextField()
    content = models.TextField()
    author = models.TextField()
    classification = models.TextField()
    modified = models.BooleanField(default=False)

    def __str__(self):
        return str(self.nid)

<<<<<<< HEAD
    def save(self,*args,**kwargs):
        time = datetime.datetime.now().replace(tzinfo=datetime.timezone(datetime.timedelta(hours=8)))
        if not self.nid:
            self.created_time = time 
        self.modified_time = time
        return super(NewsModel,self).save(*args,**kwargs)
=======
    def save(self, *args, **kwargs):
        if not self.nid:
            self.created_time = datetime.datetime.now().replace(tzinfo=datetime.timezone(datetime.timedelta(hours=8)))
        else:
            self.modified = True
        self.modified_time = datetime.datetime.now().replace(tzinfo=datetime.timezone(datetime.timedelta(hours=8)))
        return super(NewsModel, self).save(*args, **kwargs)
>>>>>>> 3ae4fbeb0e3a3f249320a635a1d0b36908bdb434
