# Generated by Django 2.2.2 on 2019-08-05 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Match', '0005_match_sport'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='closed',
            field=models.BooleanField(default=False),
        ),
    ]
