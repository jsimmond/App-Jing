# Generated by Django 2.2.2 on 2019-08-05 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Sport', '0001_initial'),
        ('Match', '0004_auto_20190805_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='sport',
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to='Sport.Sport'),
            preserve_default=False,
        ),
    ]
