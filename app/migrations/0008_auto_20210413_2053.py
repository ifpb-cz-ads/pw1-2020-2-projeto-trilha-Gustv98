# Generated by Django 3.1.7 on 2021-04-13 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20210413_0926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmes',
            name='diretor',
            field=models.CharField(max_length=50, null=True),
        ),
    ]