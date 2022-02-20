from platform import machine
from django.shortcuts import render
import pandas as pd
from dashboard.models import Utilization, Samples, Revenue, MissedRevenue, stats, monthlystats
from dashboard.serializers import UtilizationSerializer, SamplesSerializer, RevenueSerializer, MissedSerializer, statsSerializer, monthlystatsSerializer
# Create your views here.




def indexpage(request):
    samples_obj = Samples.objects.all()
    revenue_obj = Revenue.objects.all()
    samples_serializer = SamplesSerializer(samples_obj, many=True)
    revenue_serializer = RevenueSerializer(revenue_obj, many=True)

    samples_df = pd.DataFrame(samples_serializer.data)
    revenue_df = pd.DataFrame(revenue_serializer.data)

    if request.method == 'POST':

        YEAR = request.POST['year']
        MONTH = request.POST['month']
        MACHINE = request.POST['assay']

        years = samples_df['Year'].unique()
        machines = samples_df['MachineID'].unique()
        months = [col for col in samples_df.columns if col not in ('AssayID', 'Assay', 'Year', 'MachineID')]

        samples_year = samples_df.loc[samples_df['Year'] == int(YEAR)]
        machine_index = samples_year[[MONTH, 'MachineID']]
        monthly_index = samples_year.loc[samples_year['MachineID'] == MACHINE]
        monthly_index = monthly_index.loc[:, ~((monthly_index.columns == 'Assay') | (monthly_index.columns == 'Year') | (monthly_index.columns == 'AssayID') | (monthly_index.columns == 'MachineID'))]


        revenue_year = revenue_df.loc[revenue_df['Year'] == int(YEAR)]
        revenue_only = revenue_year.loc[:, ~((revenue_year.columns == 'Assay') | (revenue_year.columns == 'Year') | (revenue_year.columns == 'MachineID') )]

        yearly_revenue = revenue_only.sum(axis=1, numeric_only=True)
        revenue_labels = revenue_year['MachineID']
        y = yearly_revenue.values

        context = {
            'years': years,
            'Machines': machines,
            'Months': months,
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

            yearly_revenue = revenue_only.sum(axis=1, numeric_only=True)
            revenue_labels = revenue_year['MachineID']
            y = yearly_revenue.values


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
    samples_obj = Samples.objects.all()
    monthlystats_obj = monthlystats.objects.all()

    samples_serializer = SamplesSerializer(samples_obj, many=True)
    monthlystats_serializer = monthlystatsSerializer(monthlystats_obj, many=True)

    samples_df = pd.DataFrame(samples_serializer.data)
    monthlystats_df = pd.DataFrame(monthlystats_serializer.data)

    
    if request.method == 'POST':
        YEAR = request.POST['year']
        MONTH = request.POST['month']

        years = samples_df['Year'].unique()
        months = [col for col in samples_df.columns if col not in ('AssayID', 'Assay', 'Year', 'MachineID')]
        machines = samples_df['MachineID'].unique()

        samples_year = samples_df.loc[samples_df['Year'] == int(YEAR)]
        machine_samples = samples_year[[MONTH, 'MachineID']]

        maxmonthly_samples = monthlystats_df['MaxMonthSamples'].values
        collected_samples = machine_samples[MONTH].values

        missed_samples = maxmonthly_samples - collected_samples

        context = {
            'years': years,
            'Months': months,
            'Machines': machines,
            'sel_year': YEAR,
            'sel_month': MONTH,
            'machine_labels': machine_samples['MachineID'].to_list(),
            'collected_samples': collected_samples,
            'missed_samples': missed_samples

        }

        return render(request, 'dashboard/sample.html', context)
    else:
        if samples_df.empty:
            return render(request, 'dashboard/sample.html', {})
        else:
            years = samples_df['Year'].unique()
            months = [col for col in samples_df.columns if col not in ('AssayID', 'Assay', 'Year', 'MachineID')]
            machines = samples_df['MachineID'].unique()

            samples_year = samples_df.loc[samples_df['Year'] == years[0]]
            machine_samples = samples_year[[months[0], 'MachineID']]

            maxmonthly_samples = monthlystats_df['MaxMonthSamples'].values
            collected_samples = machine_samples[months[0]].values

            missed_samples = maxmonthly_samples - collected_samples

            context = {
                'years': years,
                'Months': months,
                'Machines': machines,
                'sel_year': years[0],
                'sel_month': months[0],
                'machine_labels': machine_samples['MachineID'].to_list(),
                'collected_samples': machine_samples[months[0]].to_list(),
                'missed_samples': missed_samples
                
            }

            return render(request, 'dashboard/sample.html', context)


def util(request):
    util_obj = Utilization.objects.all()
    monthlystats_obj = monthlystats.objects.all()

    util_serializer = UtilizationSerializer(util_obj, many=True)
    monthlystats_serializer = monthlystatsSerializer(monthlystats_obj, many=True)

    util_df = pd.DataFrame(util_serializer.data)
    monthlystats_df = pd.DataFrame(monthlystats_serializer.data)

    if request.method == 'POST':
        YEAR = request.POST['year']
        MONTH = request.POST['month']

        years = util_df['Year'].unique()
        months = [col for col in util_df.columns if col not in ('AssayID', 'Assay', 'Year', 'MachineID')]
        machines = util_df['MachineID'].unique()

        samples_year = util_df.loc[util_df['Year'] == int(YEAR)]
        machine_util = samples_year[[MONTH, 'MachineID']]

        maxmonthly_util = monthlystats_df['MaxMonthlyhours'].values
        actual_utilizition = machine_util[MONTH].values

        missed_util = maxmonthly_util - actual_utilizition

        context = {
            'years': years,
            'Months': months,
            'Machines': machines,
            'sel_year': YEAR,
            'sel_month': MONTH,
            'machine_labels': machine_util['MachineID'].to_list(),
            'actual_utilization': actual_utilizition,
            'missed_util': missed_util

        }

        return render(request, 'dashboard/utilization.html', context)
    else:
        if util_df.empty:
            return render(request, 'dashboard/utilization.html', {})
        else:
            years = util_df['Year'].unique()
            months = [col for col in util_df.columns if col not in ('AssayID', 'Assay', 'Year', 'MachineID')]
            machines = util_df['MachineID'].unique()

            samples_year = util_df.loc[util_df['Year'] == years[0]]
            machine_util = samples_year[[months[0], 'MachineID']]

            maxmonthly_util = monthlystats_df['MaxMonthlyhours'].values
            actual_utilizition = machine_util[months[0]].values

            missed_util = maxmonthly_util - actual_utilizition

            context = {
            'years': years,
            'Months': months,
            'Machines': machines,
            'sel_year': years[0],
            'sel_month': months[0],
            'machine_labels': machine_util['MachineID'].to_list(),
            'actual_utilization': actual_utilizition,
            'missed_util': missed_util

            }

            return render(request, 'dashboard/utilization.html', context)


def revenue(request):
    revenue_obj = Revenue.objects.all()
    monthlystats_obj = monthlystats.objects.all()

    revenue_serializer = RevenueSerializer(revenue_obj, many=True)
    monthlystats_serializer = monthlystatsSerializer(monthlystats_obj, many=True)

    revenue_df = pd.DataFrame(revenue_serializer.data)
    monthlystats_df = pd.DataFrame(monthlystats_serializer.data)

    if request.method == 'POST':
        YEAR = request.POST['year']
        MONTH = request.POST['month']

        years = revenue_df['Year'].unique()
        months = [col for col in revenue_df.columns if col not in ('AssayID', 'Assay', 'Year', 'MachineID')]
        machines = revenue_df['MachineID'].unique()

        samples_year = revenue_df.loc[revenue_df['Year'] == int(YEAR)]
        machine_revenue = samples_year[[MONTH, 'MachineID']]

        maxmonthly_revenue = monthlystats_df['MaxMonthlyRevenue'].values
        actual_revenue = machine_revenue[MONTH].values

        missed_revenue = maxmonthly_revenue - actual_revenue

        context = {
            'years': years,
            'Months': months,
            'Machines': machines,
            'sel_year': YEAR,
            'sel_month': MONTH,
            'machine_labels': machine_revenue['MachineID'].to_list(),
            'actual_revenue': actual_revenue,
            'missed_revenue': missed_revenue

        }

        return render(request, 'dashboard/revenue.html', context)
    else:
        if revenue_df.empty:
            return render(request, 'dashboard/revenue.html')
        else:
            years = revenue_df['Year'].unique()
            months = [col for col in revenue_df.columns if col not in ('AssayID', 'Assay', 'Year', 'MachineID')]
            machines = revenue_df['MachineID'].unique()

            samples_year = revenue_df.loc[revenue_df['Year'] == years[0]]
            machine_revenue = samples_year[[months[0], 'MachineID']]

            maxmonthly_revenue = monthlystats_df['MaxMonthlyRevenue'].values
            actual_revenue = machine_revenue[months[0]].values

            missed_revenue = maxmonthly_revenue - actual_revenue
            context = {
                'years': years,
                'Months': months,
                'Machines': machines,
                'sel_year': years[0],
                'sel_month': months[0],
                'machine_labels': machine_revenue['MachineID'].to_list(),
                'actual_revenue': actual_revenue,
                'missed_revenue': missed_revenue

            }
            return render(request, 'dashboard/revenue.html', context)



