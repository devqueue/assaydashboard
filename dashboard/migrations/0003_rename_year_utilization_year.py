# Generated by Django 4.0.2 on 2022-02-02 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_utilization_year'),
    ]

    operations = [
        migrations.RenameField(
            model_name='utilization',
            old_name='year',
            new_name='Year',
        ),
    ]
