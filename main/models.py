from django.db import models

# Create your models here.

class Circle(models.Model):
    x = models.FloatField('Координата X', max_length=10)
    y = models.FloatField('Координата Y', max_length=10)
    r = models.FloatField('Радиус окружности', max_length=10)

