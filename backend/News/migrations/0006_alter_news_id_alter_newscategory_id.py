# Generated by Django 4.0.4 on 2022-05-17 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0005_auto_20190717_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='newscategory',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
