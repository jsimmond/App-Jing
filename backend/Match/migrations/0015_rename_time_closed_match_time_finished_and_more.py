# Generated by Django 4.0.4 on 2022-08-08 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Match', '0014_remove_match_teams_matchteam_match'),
    ]

    operations = [
        migrations.RenameField(
            model_name='match',
            old_name='time_closed',
            new_name='time_finished',
        ),
        migrations.RemoveField(
            model_name='match',
            name='length',
        ),
        migrations.RemoveField(
            model_name='match',
            name='state',
        ),
        migrations.AddField(
            model_name='match',
            name='played',
            field=models.BooleanField(default=False),
        ),
    ]
