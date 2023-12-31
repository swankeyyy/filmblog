# Generated by Django 3.1.5 on 2023-09-15 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_genre'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(db_index=True, max_length=30, verbose_name='Пункт меню')),
                ('slug', models.SlugField(max_length=30, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Пункты меню',
            },
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'verbose_name': 'Жанры'},
        ),
    ]
