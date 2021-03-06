# Generated by Django 2.2 on 2019-07-18 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('year', models.PositiveIntegerField()),
                ('logo', models.ImageField(upload_to='events/')),
            ],
        ),
    ]
