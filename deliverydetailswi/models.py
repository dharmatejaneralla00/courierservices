from django.db import models

# Create your models here.
class Delupdate(models.Model):
    conno = models.CharField(max_length=15,unique=True,null=False)
    recby = models.CharField(max_length=100)
    deldate = models.CharField(max_length=10)
    