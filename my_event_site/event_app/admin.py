from django.contrib import admin

from .models import Event, List, Item, Person, Guestlist

# allows us to see  model in admin interface
admin.site.register(Event)
admin.site.register(List)
admin.site.register(Item)
admin.site.register(Person)
admin.site.register(Guestlist)