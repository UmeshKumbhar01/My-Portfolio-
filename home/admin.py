from django.contrib import admin
from . import models


# Register your models here.
class Result_admin(admin.ModelAdmin):
    list_display = ['ssc_mark','Dip_mark','Eng_mark']

admin.site.register(models.Results_model,Result_admin)