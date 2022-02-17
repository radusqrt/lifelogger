from django.contrib import admin

from .models import Event, Sleep, SymptomGroup, Food, Recipe, Activity

admin.site.register(Event)
admin.site.register(Sleep)
admin.site.register(SymptomGroup)
admin.site.register(Food)
admin.site.register(Recipe)
admin.site.register(Activity)
