from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.User)

# different from above, python manage.py createsuperuser
# admin hhyzuishuai
