from django.db import models

from .lib.AvailableEntities import AVAILABLE_ENTITIES

# Create your models here.

class UserDefinedEntity(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(blank=True, max_length=256)
    entity_type = models.CharField(
        max_length=64,
        choices=AVAILABLE_ENTITIES,
        default="img"
    )

    def __str__(self):
        return self.name

class Label(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(blank=True, max_length=128)
    weight = models.FloatField(blank=True, default=1.0)

    def __str__(self):
        return self.name

class Dataset(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Datapoint(models.Model):
    entity_type = models.ForeignKey(UserDefinedEntity, on_delete=models.CASCADE, default='')
    data = models.TextField()
    name = models.CharField(blank=True, max_length=128)
    description = models.CharField(blank=True, max_length=256)
    active = models.BooleanField(default=True)
    labels = models.ManyToManyField(Label, blank=True)
    added = models.DateTimeField(auto_now_add=True)
    dataset = models.ManyToManyField(Dataset, blank=True)

    def __str__(self):
        return self.name