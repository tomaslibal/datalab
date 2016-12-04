from django.contrib import admin
from .models import UserDefinedEntity, Datapoint, Label, Dataset

# Register your models here.
admin.site.register(UserDefinedEntity)
admin.site.register(Datapoint)
admin.site.register(Label)
admin.site.register(Dataset)

