from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import pandas as pd
from dashboard.models import Utilization, Samples, Revenue, MissedRevenue
from dashboard.serializers import UtilizationSerializer, SamplesSerializer, RevenueSerializer, MissedSerializer
# Create your views here.



def indexpage(request):
    if request.method == 'GET':
        samples_obj = Samples.objects.all()
        samples_serializer = SamplesSerializer(samples_obj, many=True)
        samples_df = pd.DataFrame(samples_serializer.data)

        context = {
            'years': samples_df['Year'].unique(),
            'Assay': samples_df['Assay'].unique(),
            'Months': [col for col in samples_df.columns if col not in ('AssayID', 'Assay', 'Year')]
        }
        print(context['Months'])
        return render(request, 'dashboard/index.html', context)


def sample(request):
    if request.method == 'GET':

        return render(request, 'dashboard/sample.html')

def util(request):
    if request.method == 'GET':

        return render(request, 'dashboard/utilization.html')

def revenue(request):
    if request.method == 'GET':

        return render(request, 'dashboard/revenue.html')



