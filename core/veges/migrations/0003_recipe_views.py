# Generated by Django 5.1.3 on 2024-12-16 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veges', '0002_recipe_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]