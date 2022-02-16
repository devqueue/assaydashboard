from django.db import models
import datetime
# Create your models here.

def current_year():
    return datetime.date.today().year


class Samples(models.Model):
    AssayID = models.CharField(primary_key=True, max_length=10)
    Assay = models.CharField(max_length=100)
    January = models.FloatField()
    February = models.FloatField()
    March = models.FloatField()
    April = models.FloatField()
    May = models.FloatField()
    June = models.FloatField()
    July = models.FloatField()
    August = models.FloatField()
    September = models.FloatField()
    October = models.FloatField()
    November = models.FloatField()
    December = models.FloatField()
    Year = models.IntegerField(default=current_year)


class Utilization(models.Model):
    AssayID = models.CharField(primary_key=True, max_length=10)
    Assay = models.CharField(max_length=100)
    January = models.FloatField()
    February = models.FloatField()
    March = models.FloatField()
    April = models.FloatField()
    May = models.FloatField()
    June = models.FloatField()
    July = models.FloatField()
    August = models.FloatField()
    September = models.FloatField()
    October = models.FloatField()
    November = models.FloatField()
    December = models.FloatField()
    Year = models.IntegerField(default=current_year)


class Revenue(models.Model):
    AssayID = models.CharField(primary_key=True, max_length=10)
    Assay = models.CharField(max_length=100)
    January = models.FloatField()
    February = models.FloatField()
    March = models.FloatField()
    April = models.FloatField()
    May = models.FloatField()
    June = models.FloatField()
    July = models.FloatField()
    August = models.FloatField()
    September = models.FloatField()
    October = models.FloatField()
    November = models.FloatField()
    December = models.FloatField()
    Year = models.IntegerField(default=current_year)

class MissedRevenue(models.Model):
    AssayID = models.CharField(primary_key=True, max_length=10)
    Assay = models.CharField(max_length=100)
    January = models.FloatField()
    February = models.FloatField()
    March = models.FloatField()
    April = models.FloatField()
    May = models.FloatField()
    June = models.FloatField()
    July = models.FloatField()
    August = models.FloatField()
    September = models.FloatField()
    October = models.FloatField()
    November = models.FloatField()
    December = models.FloatField()
    Year = models.IntegerField(default=current_year)


class stats(models.Model):
    AssayID = models.CharField(primary_key=True, max_length=10)
    FullCapacity = models.FloatField()
    RunTime = models.FloatField()
    Price = models.FloatField()

class monthlystats(models.Model):
    AssayID = models.CharField(primary_key=True, max_length=10)
    MaxMonthlyhours = models.FloatField()
    MaxMonthlyRevenue = models.FloatField()
    MaxMonthSamples = models.FloatField()