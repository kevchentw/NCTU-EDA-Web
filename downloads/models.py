from django.db import models

# Create your models here.
class DownloadsModel(models.Model):
    did = models.AutoField(primary_key=True)
    filename = models.TextField()
    description = models.TextField()
    uploader = models.TextField()
    classification = models.TextField()
    modified = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True, editable=True)

    def __str__(self):
        return str(self.did)

    def save(self, *args, **kwargs):
        if self.nid:
            self.modified = True
        return super(DownloadsModel, self).save(*args, **kwargs)
