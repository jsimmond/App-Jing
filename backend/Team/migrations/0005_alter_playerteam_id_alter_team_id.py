# Generated by Django 4.0.4 on 2022-05-17 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Team', '0004_auto_20190819_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playerteam',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='team',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
