# Generated by Django 5.0.1 on 2024-04-12 03:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_ownerprofile_user_alter_userprofile_user_and_more'),
        ('contact', '0035_remove_owner_social_media_links'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='ownerprofile',
            name='owner',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='owner_profile', to='contact.owner', verbose_name='Eigentümer'),
        ),
        migrations.AlterField(
            model_name='ownerprofile',
            name='user',
            field=models.OneToOneField(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='owner_user_profile', to=settings.AUTH_USER_MODEL, verbose_name='Benutzer'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_profile', to=settings.AUTH_USER_MODEL, verbose_name='Benutzer'),
        ),
    ]
