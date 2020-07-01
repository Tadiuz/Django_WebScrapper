from django.contrib import admin

from .models import Search
# Register your models here.

#Here we are integrating the Search model thta we created into the admin console so we can manage it from there
admin.site.register(Search)