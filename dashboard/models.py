from django.db import models
import datetime
# Create your models here.

def current_year():
    return datetime.date.today().year


class Samples(models.Model):
    TestID = models.CharField(primary_key=True, max_length=10)
    Test = models.CharField(max_length=100)
    January = models.FloatField()
    February = models.FloatField()
    March = models.FloatField()
    April = models.FloatField()
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
    June = models.FloatField()
    July = models.FloatField()
    August = models.FloatField()
    September = models.FloatField()
    October = models.FloatField()
    November = models.FloatField()
    December = models.FloatField()
    Year = models.IntegerField(default=current_year)


class Revenue(models.Model):
    TestID = models.CharField(primary_key=True, max_length=10)
    Test = models.CharField(max_length=100)
    January = models.FloatField()
    February = models.FloatField()
    March = models.FloatField()
    April = models.FloatField()
    June = models.FloatField()
    July = models.FloatField()
    August = models.FloatField()
    September = models.FloatField()
    October = models.FloatField()
    November = models.FloatField()
    December = models.FloatField()
    Year = models.IntegerField(default=current_year)

