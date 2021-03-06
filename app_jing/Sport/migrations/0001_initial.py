# Generated by Django 2.2.2 on 2019-07-30 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Person', '0004_person_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('MLE', 'Masculino'), ('FEM', 'Femenino'), ('MIX', 'Mixto')], default='MIX', max_length=3)),
                ('sport_type', models.CharField(choices=[('A', 'Tipo A'), ('B', 'Tipo B'), ('C', 'Tipo C')], default='A', max_length=1)),
                ('coordinator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Person.Person')),
            ],
        ),
    ]
