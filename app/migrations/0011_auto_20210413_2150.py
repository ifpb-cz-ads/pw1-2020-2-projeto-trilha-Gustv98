# Generated by Django 3.1.7 on 2021-04-14 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20210413_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmes',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
