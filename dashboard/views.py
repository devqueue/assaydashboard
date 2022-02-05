from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import pandas as pd
from dashboard.models import Utilization, Processed, Revenue
from dashboard.serializers import UtilizationSerializer, ProcessedSerializer, RevenueSerializer
# Create your views here.

@csrf_exempt
def utilizationApi(request, id=0):
    if request.method == 'GET':
        try:
            utilization = Utilization.objects.get(AssayID=id)
            utilization_serializer = UtilizationSerializer(utilization)
            utilization_df = pd.DataFrame(utilization_serializer.data, index=[0])
            data = utilization_df.select_dtypes(include ='float64').iloc[0].to_list()
            return JsonResponse(data, safe=False)
        except:
            return JsonResponse("Failed to get", safe=False)
    
    elif request.method == 'POST':
        utilization_data  = JSONParser().parse(request)
        utilization_serializer = UtilizationSerializer(data=utilization_data, many=True)

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
            

@csrf_exempt
def processedApi(request, id=0):
    if request.method == 'GET':
        try:
            processed = Processed.objects.get(TestID=id)
            processed_serializer = ProcessedSerializer(processed)
            processed_df = pd.DataFrame(processed_serializer.data, index=[0])
            data = processed_df.select_dtypes(include ='float64').iloc[0].to_list()
            return JsonResponse(data, safe=False)
        except:
            return JsonResponse("Failed to get", safe=False)
    
    elif request.method == 'POST':
        processed_data  = JSONParser().parse(request)
        processed_serializer = ProcessedSerializer(data=processed_data)

        if processed_serializer.is_valid():
            processed_serializer.save()
            return JsonResponse("Added Suceesfullly", safe=False)
        return JsonResponse("Failed to add", safe=False)
    
    elif request.method == 'PUT':
        processed_data  = JSONParser().parse(request)
        processed = Processed.objects.get(TestID=processed_data['TestID'])
        processed_serializer = ProcessedSerializer(processed, data=processed_data)

        if processed_serializer.is_valid():
            processed_serializer.save()
            return JsonResponse("Updated Suceesfullly", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    
    elif request.method == 'DELETE':
        processed = Processed.objects.get(TestID=id)
        processed.delete()
        return JsonResponse("Deleted sucessfully", safe=False)


@csrf_exempt
def revenueapi(request, id=0):
    if request.method == 'GET':
        try:
            revenue = Revenue.objects.get(TestID=id)
            revenue_serializer = RevenueSerializer(revenue)
            revenue_df = pd.DataFrame(revenue_serializer.data, index=[0])
            data = revenue_df.select_dtypes(include ='float64').iloc[0].to_list()
            return JsonResponse(data, safe=False)
        except:
            return JsonResponse("Failed to get", safe=False)
    
    elif request.method == 'POST':
        revenue_data  = JSONParser().parse(request)
        revenue_serializer = RevenueSerializer(data=revenue_data)

        if revenue_serializer.is_valid():
            revenue_serializer.save()
            return JsonResponse("Added Suceesfullly", safe=False)
        return JsonResponse("Failed to add", safe=False)
    
    elif request.method == 'PUT':
        revenue_data  = JSONParser().parse(request)
        revenue = Revenue.objects.get(TestID=revenue_data['TestID'])
        revenue_serializer = RevenueSerializer(revenue, data=revenue_data)

        if revenue_serializer.is_valid():
            revenue_serializer.save()
            return JsonResponse("Updated Suceesfullly", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    
    elif request.method == 'DELETE':
        revenue = Revenue.objects.get(TestID=id)
        revenue.delete()
        return JsonResponse("Deleted sucessfully", safe=False)



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

def processpage(request):
    processed = Processed.objects.all()
    Processed_serializer = ProcessedSerializer(processed, many=True)
    Processed_df = pd.DataFrame(Processed_serializer.data)

    label = Processed_df['Test'].to_list()

    context = {"label": zip(label, range(1, len(label))), 
               "labels": Processed_df.select_dtypes(include ='float64').columns.to_list(),
               "data": Processed_df.loc[Processed_df['TestID'] == 1].select_dtypes(include ='float64').iloc[0].to_list(),
    }
    if request.method == 'GET':

        return render(request, 'processed.html', context)


def revenuepage(request):
    revenue = Revenue.objects.all()
    revenue_serializer = RevenueSerializer(revenue, many=True)
    revenue_df = pd.DataFrame(revenue_serializer.data)
    label = revenue_df['Test'].to_list()

    context = {"label": zip(label, range(1, len(label))), 
               "labels": revenue_df.select_dtypes(include ='float64').columns.to_list(),
               "data": revenue_df.loc[revenue_df['TestID'] == 1].select_dtypes(include ='float64').loc[0].to_list(),
    }
    if request.method == 'GET':

        return render(request, 'revenue.html', context)