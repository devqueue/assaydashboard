# Generated by Django 4.0.2 on 2022-02-05 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_processed_revenue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processed',
            name='TestID',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='revenue',
            name='TestID',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='utilization',
            name='AssayID',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
