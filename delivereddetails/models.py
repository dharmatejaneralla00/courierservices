from django.db import models

# Create your models here.
class RecievedDetails(models.Model):
    delivereddate = models.CharField(max_length=30)
    recievedby = models.CharField(max_length=50)
    consignmentnumber = models.CharField(max_length=30,null=False,unique=True)
    def __str__(self):
        return self.consignmentnumber