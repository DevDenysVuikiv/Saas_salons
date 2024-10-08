# Generated by Django 5.0.1 on 2024-04-07 02:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_user_alter_ownerprofile_user_alter_userprofile_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='ownerprofile',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='owner_user_profile', to=settings.AUTH_USER_MODEL, verbose_name='Benutzer'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL, verbose_name='Benutzer'),
        ),
        migrations.AddField(
            model_name='ownerprofile',
            name='address',
            field=models.TextField(blank=True, null=True, verbose_name='Adresse'),
        ),
        migrations.AddField(
            model_name='ownerprofile',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='Geburtsdatum'),
        ),
        migrations.AddField(
            model_name='ownerprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Männlich'), ('female', 'Weiblich')], max_length=10, null=True, verbose_name='Geschlecht'),
        ),
        migrations.AddField(
            model_name='ownerprofile',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefon'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='address',
            field=models.TextField(blank=True, null=True, verbose_name='Adresse'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='Geburtsdatum'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Männlich'), ('female', 'Weiblich')], max_length=10, null=True, verbose_name='Geschlecht'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefon'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
