from django.db import models

# Create your models here.

class Entity(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(blank=True, max_length=256)

    def __str__(self):
        return self.name

class Label(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(blank=True, max_length=128)
    weight = models.FloatField(blank=True, default=1.0)

    def __str__(self):
        return self.name

class Datapoint(models.Model):
    entity_type = models.ForeignKey(Entity, on_delete=models.CASCADE, default='')
    data = models.TextField()
    name = models.CharField(blank=True, max_length=128)
    description = models.CharField(blank=True, max_length=256)
    active = models.BooleanField(default=True)
    labels = models.ManyToManyField(Label, blank=True)

    def __str__(self):
        return self.description


