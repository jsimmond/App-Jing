# Generated by Django 2.2 on 2019-06-17 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=30)),
                ('overall_score', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UniversityLogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='university_logo/')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='University.University')),
            ],
        ),
    ]
