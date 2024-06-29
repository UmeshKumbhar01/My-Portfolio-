from django.db import models


# Create your models here.
class Results_model(models.Model):
    ssc_mark = models.IntegerField()
    Dip_mark = models.IntegerField()
    Eng_mark = models.IntegerField()
