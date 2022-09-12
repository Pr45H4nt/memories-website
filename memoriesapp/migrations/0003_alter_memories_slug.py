# Generated by Django 4.1 on 2022-09-12 03:10

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memoriesapp', '0002_memories_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memories',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from=models.CharField(max_length=300), unique=True),
        ),
    ]