# Generated by Django 3.0.8 on 2020-07-29 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='circle',
            name='r',
            field=models.FloatField(max_length=10, verbose_name='Радиус окружности'),
        ),
        migrations.AlterField(
            model_name='circle',
            name='x',
            field=models.FloatField(max_length=10, verbose_name='Координата X'),
        ),
        migrations.AlterField(
            model_name='circle',
            name='y',
            field=models.FloatField(max_length=10, verbose_name='Координата Y'),
        ),
    ]
