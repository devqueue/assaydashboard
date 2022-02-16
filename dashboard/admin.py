from django.contrib import admin
from .models import Samples, Revenue, Utilization, stats, monthlystats, MissedRevenue
# Register your models here.

admin.site.register([Samples, Revenue, Utilization, stats, monthlystats, MissedRevenue])