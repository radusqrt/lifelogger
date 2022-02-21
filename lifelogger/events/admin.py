from django.contrib import admin
from .models import Activity, Event, Food, Recipe, Sleep, Sport, SymptomGroup

# Register your models here.
admin.site.register(Event)
admin.site.register(Sleep)
admin.site.register(Sport)
admin.site.register(Activity)
admin.site.register(Food)
admin.site.register(Recipe)
admin.site.register(SymptomGroup)
