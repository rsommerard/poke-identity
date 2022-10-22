from django.contrib import admin
from django.contrib.admin import ModelAdmin

from users import models


@admin.register(models.User)
class User(ModelAdmin):
    pass
