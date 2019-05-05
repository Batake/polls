from django.contrib import admin

from .models import Dinner, Menu
# Register your models here.

admin.site.register([Dinner, Menu])