# Generated by Django 4.2 on 2023-08-04 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='modulo',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]