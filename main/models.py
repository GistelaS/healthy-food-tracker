from django.db import models

# Create your models here.
from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    calories = models.IntegerField()
    description = models.TextField()