# Generated by Django 4.2.6 on 2024-08-07 22:14

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
                ('recipe_name', models.CharField(max_length=100)),
                ('recipe_desp', models.TextField()),
                ('recipe_img', models.ImageField(upload_to='')),
            ],
        ),
    ]
