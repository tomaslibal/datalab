from django.contrib import admin
from .models import Entity, Datapoint, Label

# Register your models here.
admin.site.register(Entity)
admin.site.register(Datapoint)
admin.site.register(Label)

