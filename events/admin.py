from django.contrib import admin

from .models import Event, Sleep, SymptomGroup

admin.site.register(Event)
admin.site.register(Sleep)
admin.site.register(SymptomGroup)
