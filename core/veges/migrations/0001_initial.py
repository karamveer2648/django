# Generated by Django 5.1.3 on 2024-12-13 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ingredients', models.TextField()),
                ('prep_time', models.CharField(max_length=100)),
                ('prep_guide', models.TextField()),
                ('image', models.ImageField(upload_to='recipe_images/')),
                ('category', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
