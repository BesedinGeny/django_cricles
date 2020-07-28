from django.db import models

# Create your models here.

class Circle(models.Model):
    x = models.CharField('Координата X', max_length=10)
    y = models.CharField('Координата Y', max_length=10)
    r = models.CharField('Радиус окружности', max_length=10)

