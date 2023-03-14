from django.contrib import admin
from django.contrib.auth.models import Group
from myskool.models import MySkool

# Register your models here.

admin.site.unregister([Group])
admin.site.register([MySkool])