from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class NewsModel(models.Model):
    nid = models.AutoField(primary_key = True)
    top = models.BooleanField(default = False)
    created_time = models.DateTimeField(editable = False)
    modified_time = models.DateTimeField()
    title = models.TextField()
    content = models.TextField()
    author = models.TextField()
    classification = models.TextField()

    def __str__(self):
        return str(self.nid)

    def save(self,*args,**kwargs):
        time = datetime.datetime.now().replace(tzinfo=datetime.timezone(datetime.timedelta(hours=8)))
        if not self.nid:
            self.created_time = time 
        self.modified_time = time
        return super(NewsModel,self).save(*args,**kwargs)
