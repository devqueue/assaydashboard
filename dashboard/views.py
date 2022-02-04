from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import pandas as pd
from dashboard.models import Utilization
from dashboard.serializers import UtilizationSerializer
# Create your views here.

@csrf_exempt
def utilizationApi(request, id=0, **kwargs):
    if request.method == 'GET':
        utilization = Utilization.objects.get(AssayID=id)
        utilization_serializer = UtilizationSerializer(utilization)
        utilization_df = pd.DataFrame(utilization_serializer.data, index=[0])
        data = utilization_df.select_dtypes(include ='float64').iloc[0].to_list()
        return JsonResponse(data, safe=False)
    
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
            

from pprint import pprint as pp
def indexpage(request):
    utilization = Utilization.objects.all()
    utilization_serializer = UtilizationSerializer(utilization, many=True)
    utilization_df = pd.DataFrame(utilization_serializer.data)
    label = utilization_df['Assay'].to_list()

    context = {"label": zip(label, range(1, len(label))), 
               "labels": utilization_df.select_dtypes(include ='float64').columns.to_list(),
               "data": utilization_df.loc[utilization_df['AssayID'] == 1].select_dtypes(include ='float64').loc[0].to_list(),
    }
    if request.method == 'GET':

        return render(request, 'index.html', context)
