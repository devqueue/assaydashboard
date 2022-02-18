from platform import machine
from django.shortcuts import render
import pandas as pd
from dashboard.models import Utilization, Samples, Revenue, MissedRevenue
from dashboard.serializers import UtilizationSerializer, SamplesSerializer, RevenueSerializer, MissedSerializer
# Create your views here.




def indexpage(request):
    if request.method == 'POST':

        YEAR = request.POST['year']
        MONTH = request.POST['month']
        MACHINE = request.POST['assay']
        
        samples_obj = Samples.objects.all()
        revenue_obj = Revenue.objects.all()
        samples_serializer = SamplesSerializer(samples_obj, many=True)
        revenue_serializer = RevenueSerializer(revenue_obj, many=True)

        samples_df = pd.DataFrame(samples_serializer.data)
        revenue_df = pd.DataFrame(revenue_serializer.data)


        samples_year = samples_df.loc[samples_df['Year'] == int(YEAR)]
        machine_index = samples_year[[MONTH, 'MachineID']]
        monthly_index = samples_year.loc[samples_year['MachineID'] == MACHINE]
        monthly_index = monthly_index.loc[:, ~((monthly_index.columns == 'Assay') | (monthly_index.columns == 'Year') | (monthly_index.columns == 'AssayID') | (monthly_index.columns == 'MachineID'))]


        revenue_year = revenue_df.loc[revenue_df['Year'] == int(YEAR)]
        revenue_only = revenue_year.loc[:, ~((revenue_year.columns == 'Assay') | (revenue_year.columns == 'Year') | (revenue_year.columns == 'MachineID') )]

        yearly_revenue = revenue_only.sum(axis=1)
        revenue_labels = revenue_year['MachineID']
        y = yearly_revenue.values

        context = {
            'years': samples_df['Year'].unique(),
            'Machines': samples_df['MachineID'].unique(),
            'Months': [col for col in samples_df.columns if col not in ('AssayID', 'Assay', 'Year' , 'MachineID')],
            'sel_year': YEAR,
            'sel_month': MONTH,
            'sel_machine': MACHINE,
            'machine_index': machine_index[MONTH].to_list(),
            'machine_labels': machine_index['MachineID'].to_list(),
            'monthly_index': monthly_index.values.reshape(12).tolist(),
            'monthly_labels': monthly_index.columns.tolist(),
            'revenue_lables': revenue_labels.to_list(),
            'revenue_values': list(y)
        }
        return render(request, 'dashboard/index.html', context)

    else:
        samples_obj = Samples.objects.all()
        revenue_obj = Revenue.objects.all()
        samples_serializer = SamplesSerializer(samples_obj, many=True)
        revenue_serializer = RevenueSerializer(revenue_obj, many=True)

        samples_df = pd.DataFrame(samples_serializer.data)
        revenue_df = pd.DataFrame(revenue_serializer.data)


        if samples_df.empty:
            return render(request, 'dashboard/index.html', {})

        else:
            years = samples_df['Year'].unique()
            machines = samples_df['MachineID'].unique()
            months = [col for col in samples_df.columns if col not in ('AssayID', 'Assay', 'Year', 'MachineID')]

            samples_year = samples_df.loc[samples_df['Year'] == years[0]]
            machine_index = samples_year[[months[0], 'MachineID']]
            monthly_index = samples_year.loc[samples_year['MachineID'] == machines[0]]
            monthly_index = monthly_index.loc[:, ~((monthly_index.columns == 'Assay') | (monthly_index.columns == 'Year') | (monthly_index.columns == 'AssayID') | (monthly_index.columns == 'MachineID'))]


            revenue_year = revenue_df.loc[revenue_df['Year'] == years[0]]
            revenue_only = revenue_year.loc[:, ~((revenue_year.columns == 'Assay') | (revenue_year.columns == 'Year') | (revenue_year.columns == 'MachineID') )]

            yearly_revenue = revenue_only.sum(axis=1)
            revenue_labels = revenue_year['MachineID']
            y = yearly_revenue.values

            print(revenue_only)

            context = {
                'years': years,
                'Machines': machines,
                'Months': months,
                'sel_year': years[0],
                'sel_month': months[0],
                'sel_machine': machines[0],
                'machine_index': machine_index[months[0]].to_list(),
                'machine_labels': machine_index['MachineID'].to_list(),
                'monthly_index': monthly_index.values.reshape(12).tolist(),
                'monthly_labels': monthly_index.columns.tolist(),
                'revenue_lables': revenue_labels.to_list(),
                'revenue_values': list(y)
            }

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



