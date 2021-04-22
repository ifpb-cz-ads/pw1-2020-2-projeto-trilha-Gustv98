# Generated by Django 3.1.7 on 2021-04-22 22:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0011_auto_20210413_2150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filmes',
            name='favorite',
        ),
        migrations.AlterField(
            model_name='filmes',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='filmes',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]