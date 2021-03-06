# Generated by Django 4.0.2 on 2022-04-11 15:16

import dashboard.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MissedRevenue',
            fields=[
                ('AssayID', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('MachineID', models.CharField(max_length=100)),
                ('Assay', models.CharField(max_length=100)),
                ('January', models.FloatField()),
                ('February', models.FloatField()),
                ('March', models.FloatField()),
                ('April', models.FloatField()),
                ('May', models.FloatField()),
                ('June', models.FloatField()),
                ('July', models.FloatField()),
                ('August', models.FloatField()),
                ('September', models.FloatField()),
                ('October', models.FloatField()),
                ('November', models.FloatField()),
                ('December', models.FloatField()),
                ('Year', models.IntegerField(default=dashboard.models.current_year)),
            ],
        ),
        migrations.CreateModel(
            name='monthlystats',
            fields=[
                ('AssayID', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('MachineID', models.CharField(max_length=100)),
                ('MaxMonthlyhours', models.FloatField()),
                ('MaxMonthlyRevenue', models.FloatField()),
                ('MaxMonthSamples', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Revenue',
            fields=[
                ('AssayID', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('MachineID', models.CharField(max_length=100)),
                ('Assay', models.CharField(max_length=100)),
                ('January', models.FloatField()),
                ('February', models.FloatField()),
                ('March', models.FloatField()),
                ('April', models.FloatField()),
                ('May', models.FloatField()),
                ('June', models.FloatField()),
                ('July', models.FloatField()),
                ('August', models.FloatField()),
                ('September', models.FloatField()),
                ('October', models.FloatField()),
                ('November', models.FloatField()),
                ('December', models.FloatField()),
                ('Year', models.IntegerField(default=dashboard.models.current_year)),
            ],
        ),
        migrations.CreateModel(
            name='Samples',
            fields=[
                ('AssayID', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('MachineID', models.CharField(max_length=100)),
                ('Assay', models.CharField(max_length=100)),
                ('January', models.FloatField()),
                ('February', models.FloatField()),
                ('March', models.FloatField()),
                ('April', models.FloatField()),
                ('May', models.FloatField()),
                ('June', models.FloatField()),
                ('July', models.FloatField()),
                ('August', models.FloatField()),
                ('September', models.FloatField()),
                ('October', models.FloatField()),
                ('November', models.FloatField()),
                ('December', models.FloatField()),
                ('Year', models.IntegerField(default=dashboard.models.current_year)),
            ],
        ),
        migrations.CreateModel(
            name='stats',
            fields=[
                ('AssayID', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('MachineID', models.CharField(max_length=100)),
                ('FullCapacity', models.FloatField()),
                ('RunTime', models.FloatField()),
                ('Price', models.FloatField()),
                ('Maintenance', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Utilization',
            fields=[
                ('AssayID', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('MachineID', models.CharField(max_length=100)),
                ('Assay', models.CharField(max_length=100)),
                ('January', models.FloatField()),
                ('February', models.FloatField()),
                ('March', models.FloatField()),
                ('April', models.FloatField()),
                ('May', models.FloatField()),
                ('June', models.FloatField()),
                ('July', models.FloatField()),
                ('August', models.FloatField()),
                ('September', models.FloatField()),
                ('October', models.FloatField()),
                ('November', models.FloatField()),
                ('December', models.FloatField()),
                ('Year', models.IntegerField(default=dashboard.models.current_year)),
            ],
        ),
    ]
