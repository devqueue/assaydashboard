# Generated by Django 4.0.2 on 2022-02-03 02:29

import dashboard.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_utilization_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilization',
            name='Year',
            field=models.IntegerField(default=dashboard.models.current_year),
        ),
    ]