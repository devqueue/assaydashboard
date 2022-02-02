from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from dashboard.models import Utilization
# Create your views here.

@csrf_exempt
def utilization(request, id=0):
    pass
