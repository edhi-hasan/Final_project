# Generated by Django 5.0 on 2024-10-29 21:47

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bloodology', '0021_userprofile_last_blood_donation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]
