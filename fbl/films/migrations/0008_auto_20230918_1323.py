# Generated by Django 3.1.5 on 2023-09-18 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0007_movie_typ'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(upload_to='media/%Y/%m/%d/', verbose_name='Постер'),
        ),
    ]
