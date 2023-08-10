from django.db import models

# Create your models here.
from django.db import models

class LoveCalculator(models.Model):
    person1_name = models.CharField(max_length=100)
    person2_name = models.CharField(max_length=100)
    love_percentage = models.IntegerField(default=0)
