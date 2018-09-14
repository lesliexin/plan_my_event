from django.contrib import admin

from .models import Event

# allows us to see Question model in admin interface
admin.site.register(Event)