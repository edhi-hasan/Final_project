# Generated by Django 5.0 on 2024-10-01 15:23

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bloodology', '0011_alter_user_profile_blood_gorup'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user_profile',
            new_name='UserProfile',
        ),
    ]
