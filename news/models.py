from django.db import models
from django.utils import timezone


class NewsModel(models.Model):
    nid = models.AutoField(primary_key=True)
    top = models.BooleanField(default=False)
    title = models.TextField()
    content = models.TextField()
    author = models.TextField()
    classification = models.TextField()
    modified = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True, editable=True)

    def __str__(self):
        return str(self.nid)


    def save(self, *args, **kwargs):
        if self.nid:
            self.modified = True
        return super(NewsModel, self).save(*args, **kwargs)
