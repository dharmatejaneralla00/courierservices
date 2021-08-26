from django.db import models

# Create your models here.
class Recievedata(models.Model):
    mfno = models.CharField(max_length=12, null=False)
    date = models.CharField(max_length=15)
    conno = models.CharField(max_length=15,unique=True,null=False)
    pcs = models.IntegerField()
    wt = models.CharField(max_length=5)
    def __str__(self):
        return self.conno