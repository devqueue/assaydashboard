from django.shortcuts import render
from .forms import CsvModelForm
from .models import Csv
from .processing import read_df
from dashboard.models import Samples, Revenue, Utilization
import csv
# Create your views here.


def upload_file(request):
    form = CsvModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvModelForm()
        obj = Csv.objects.get(activated=False)
        # processing 
        df = read_df(obj.file_name.path)
        
        # step 1: populate the samples
        model_instances = [Samples(
            AssayID = record['AssayID'],
            Assay = record['Assay'],
            January = record['January'],
            February = record['February'],
            March = record['March'],
            April = record['April'],
            May = record['May'],
            June = record['June'],
            July = record['July'],
            August = record['August'],
            September = record['September'],
            October = record['October'],
            November = record['November'],
            December = record['December'],
            Year = record['year']
        ) for record in df]

        Samples.objects.bulk_create(model_instances)
        
        
        # Samples.objects.create()
        # step 2: populate the revenue
        # Revenue.objects.create()
        # step 3: populate the utilization
        # Utilization.objects.create()
        # step 4: populate the missed revenue
            
        obj.activated = True
        obj.save()
    return render(request, 'upload/upload.html', {'form': form})