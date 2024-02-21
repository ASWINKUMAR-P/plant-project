from django.db import models

# Create your models here.

from django.db import models

class Tree(models.Model):
    tree_id = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    form = models.CharField(max_length=100)
    growth_rate = models.CharField(max_length=100)
    fall_color = models.CharField(max_length=100)
    environmental_tolerances = models.CharField(max_length=200)
    location_tolerances = models.CharField(max_length=200)
    notes_suggested_cultivars = models.CharField(max_length=200)
    tree_size = models.CharField(max_length=100)
    comments = models.TextField(blank=True, null=True)  # Allow null values for incomplete data

    def __str__(self):
        return self.species
