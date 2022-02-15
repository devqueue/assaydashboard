from django.contrib import admin
from .models import Samples, Revenue, Utilization
# Register your models here.

admin.site.register([Samples, Revenue, Utilization])