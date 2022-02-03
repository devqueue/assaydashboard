from tkinter import FALSE
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from dashboard.models import Utilization
from dashboard.serializers import UtilizationSerializer
# Create your views here.

@csrf_exempt
def utilizationApi(request, id=0):
    if request.method == 'GET':
        utilization = Utilization.objects.all()
        utilization_serializer = UtilizationSerializer(utilization, many=True)
        return JsonResponse(utilization_serializer.data, safe=False)
    
    elif request.method == 'POST':
        utilization_data  = JSONParser().parse(request)
        utilization_serializer = UtilizationSerializer(data=utilization_data)

        if utilization_serializer.is_valid():
            utilization_serializer.save()
            return JsonResponse("Added Suceesfullly", safe=False)
        return JsonResponse("Failed to add", safe=False)
    
    elif request.method == 'PUT':
        utilization_data  = JSONParser().parse(request)
        utilization = Utilization.objects.get(AssayID=utilization_data['AssayID'])
        utilization_serializer = UtilizationSerializer(utilization, data=utilization_data)

        if utilization_serializer.is_valid():
            utilization_serializer.save()
            return JsonResponse("Updated Suceesfullly", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    
    elif request.method == 'DELETE':
        utilization = Utilization.objects.get(AssayID=id)
        utilization.delete()
        return JsonResponse("Deleted sucessfully", safe=False)
            

