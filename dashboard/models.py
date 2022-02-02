from django.db import models

# Create your models here.
class Utilization(models.Model):
    AssayID = models.AutoField(primary_key=True)
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
    MonthlyIndex = models.FloatField()

