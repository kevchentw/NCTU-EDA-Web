from django.db import models

# Create your models here.
class testapp(models.Model):
    tid = models.AutoField(primary_key=True)
    char = models.CharField(max_length = 50)
    text = models.TextField()
    integer = models.IntegerField()
    def get_id(self):
        return int(self.tid)
    def get_char(self):
        return str(self.char)
    def __str__(self):
        return str(self.tid)+' '+str(self.char)+' '+str(self.text)+' '+str(self.integer)
