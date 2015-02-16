from django.db import models

# Create your models here.
class testapp(models.Model):
    tid = models.AutoField()
    char = models.CharField(max_length = 50)
    text = models.TextField()

