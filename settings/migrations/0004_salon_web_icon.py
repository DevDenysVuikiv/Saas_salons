# Generated by Django 5.0.1 on 2024-04-14 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_remove_salon_tax_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='salon',
            name='web_icon',
            field=models.ImageField(blank=True, null=True, upload_to='owner_logos/'),
        ),
    ]
