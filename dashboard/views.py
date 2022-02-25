from django.shortcuts import render
import pandas as pd
from dashboard.models import Utilization, Samples, Revenue, MissedRevenue, stats, monthlystats
from dashboard.serializers import UtilizationSerializer, SamplesSerializer, RevenueSerializer, MissedSerializer, statsSerializer, monthlystatsSerializer
from dashboard.viewfuncs import index_context, sample_context, util_context, revenue_context
# Create your views here.


def indexpage(request):
    samples_obj = Samples.objects.all()
    revenue_obj = Revenue.objects.all()
    samples_serializer = SamplesSerializer(samples_obj, many=True)
    revenue_serializer = RevenueSerializer(revenue_obj, many=True)

    samples_df = pd.DataFrame(samples_serializer.data)
    revenue_df = pd.DataFrame(revenue_serializer.data)

    years = samples_df['Year'].unique()
    machines = samples_df['MachineID'].unique()
    months = [col for col in samples_df.columns if col not in ('AssayID', 'Assay', 'Year', 'MachineID')]

    if request.method == 'POST':

        YEAR = request.POST['year']
        MONTH = request.POST['month']
        MACHINE = request.POST['assay']

        context = index_context(YEAR, MONTH, MACHINE, samples_df, revenue_df)
        return render(request, 'dashboard/index.html', context)

    else:
        if samples_df.empty:
            return render(request, 'dashboard/index.html', {})

        else:
            YEAR = years[0]
            MONTH = months[0]
            MACHINE = machines[0]
            context = index_context(YEAR, MONTH, MACHINE, samples_df, revenue_df)
            return render(request, 'dashboard/index.html', context)


def sample(request):
    samples_obj = Samples.objects.all()
    monthlystats_obj = monthlystats.objects.all()

    samples_serializer = SamplesSerializer(samples_obj, many=True)
    monthlystats_serializer = monthlystatsSerializer(monthlystats_obj, many=True)

    samples_df = pd.DataFrame(samples_serializer.data)
    monthlystats_df = pd.DataFrame(monthlystats_serializer.data)

    years = samples_df['Year'].unique()
    months = [col for col in samples_df.columns if col not in ('AssayID', 'Assay', 'Year', 'MachineID')]
    machines = samples_df['MachineID'].unique()

    
    if request.method == 'POST':
        YEAR = request.POST['year']
        MONTH = request.POST['month']
        YEAR2 = request.POST['year2']
        MACHINE = request.POST['assay2']

        context = sample_context(YEAR, MONTH, YEAR2, MACHINE, samples_df, monthlystats_df) 
        return render(request, 'dashboard/sample.html', context)
    else:
        if samples_df.empty:
            return render(request, 'dashboard/sample.html', {})
        else:
            YEAR = years[0]
            MONTH = months[0]
            YEAR2 = years[0]
            MACHINE = machines[0]
            context = sample_context(YEAR, MONTH, YEAR2, MACHINE, samples_df, monthlystats_df)

            return render(request, 'dashboard/sample.html', context)


def util(request):
    util_obj = Utilization.objects.all()
    monthlystats_obj = monthlystats.objects.all()

    util_serializer = UtilizationSerializer(util_obj, many=True)
    monthlystats_serializer = monthlystatsSerializer(monthlystats_obj, many=True)

    util_df = pd.DataFrame(util_serializer.data)
    monthlystats_df = pd.DataFrame(monthlystats_serializer.data)

    years = util_df['Year'].unique()
    months = [col for col in util_df.columns if col not in ('AssayID', 'Assay', 'Year', 'MachineID')]
    machines = util_df['MachineID'].unique()

    if request.method == 'POST':
        YEAR = request.POST['year']
        MONTH = request.POST['month']
        YEAR2 = request.POST['year2']
        MACHINE = request.POST['assay2']

        context = util_context(YEAR, MONTH, YEAR2 , MACHINE, util_df, monthlystats_df)

        return render(request, 'dashboard/utilization.html', context)
    else:
        if util_df.empty:
            return render(request, 'dashboard/utilization.html', {})
        else:
            YEAR = years[0]
            MONTH = months[0]
            YEAR2 = years[0]
            MACHINE = machines[0]

            context = util_context(YEAR, MONTH, YEAR2 , MACHINE, util_df, monthlystats_df)

            return render(request, 'dashboard/utilization.html', context)


def revenue(request):
    revenue_obj = Revenue.objects.all()
    monthlystats_obj = monthlystats.objects.all()

    revenue_serializer = RevenueSerializer(revenue_obj, many=True)
    monthlystats_serializer = monthlystatsSerializer(monthlystats_obj, many=True)

    revenue_df = pd.DataFrame(revenue_serializer.data)
    monthlystats_df = pd.DataFrame(monthlystats_serializer.data)

    years = revenue_df['Year'].unique()
    months = [col for col in revenue_df.columns if col not in ('AssayID', 'Assay', 'Year', 'MachineID')]
    machines = revenue_df['MachineID'].unique()

    if request.method == 'POST':
        YEAR = request.POST['year']
        MONTH = request.POST['month']
        YEAR2 = request.POST['year2']
        MACHINE = request.POST['assay2']

        context = revenue_context(YEAR, MONTH, YEAR2 , MACHINE, revenue_df, monthlystats_df)

        return render(request, 'dashboard/revenue.html', context)
    else:
        if revenue_df.empty:
            return render(request, 'dashboard/revenue.html')
        else:
            YEAR = years[0]
            MONTH = months[0]
            YEAR2 = years[0]
            MACHINE = machines[0]

            context = revenue_context(YEAR, MONTH, YEAR2 , MACHINE, revenue_df, monthlystats_df)

            return render(request, 'dashboard/revenue.html', context)



