# Generated by Django 4.0.4 on 2022-08-13 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0002_alter_event_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='closed',
            field=models.BooleanField(default=False),
        ),
    ]
