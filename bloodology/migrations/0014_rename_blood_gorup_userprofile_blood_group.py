# Generated by Django 5.0 on 2024-10-01 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bloodology', '0013_alter_userprofile_blood_gorup'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='blood_gorup',
            new_name='blood_group',
        ),
    ]
