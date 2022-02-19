from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CsvModelForm
from .models import Csv
from .processing import create_df, create_stats, calculate_revenue, calculate_utilization, get_fullcapacity, calculate_missedrevenue
from dashboard.models import Samples, Revenue, Utilization, stats, monthlystats, MissedRevenue
# Create your views here.

@login_required(login_url='accounts/login_user')
def upload_file(request):
    form = CsvModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvModelForm()
        obj = Csv.objects.get(activated=False)

        # Processing CSV FILES
         
        # Populate the stats
        try:
            df_stats = create_stats()
            stats_instances = [stats(
                AssayID = rec['AssayID'],
                MachineID = rec['MachineID'],
                Maintenance = rec['Maintenance'],
                FullCapacity = rec['Full capacity'],
                RunTime = rec['Run time'],
                Price = rec['Price']
            ) for rec in df_stats]
            try:
                stats.objects.bulk_create(stats_instances)
            except:
                stats.objects.bulk_update(stats_instances, fields=['FullCapacity', 'RunTime', 'Price', 'Maintenance'])

            # Populate the samples
            df_samples = create_df(obj.file_name.path)
            sample_instances = [Samples(
                AssayID = record['AssayID'],
                MachineID = record['MachineID'],
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
                Year = record['Year']
            ) for record in df_samples]

            try:
                Samples.objects.bulk_create(sample_instances)
            except:
                Samples.objects.bulk_update(sample_instances, 
                fields=[ 'Assay', 'January', 'February', 'March', 'April', 'May', 'June',
                'July', 'August', 'September', 'October', 'November', 'December', 'Year'])
            
            
            # Populate the revenue
            revenue_dict = calculate_revenue(df_samples, df_stats)
            Revenue_instances = [Revenue(
                AssayID = record['AssayID'],
                MachineID = record['MachineID'],
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
                Year = record['Year']
            ) for record in revenue_dict]

            try:
                Revenue.objects.bulk_create(Revenue_instances)
            except:
                Revenue.objects.bulk_update(Revenue_instances, 
                fields=[ 'Assay', 'January', 'February', 'March', 'April', 'May', 'June',
                'July', 'August', 'September', 'October', 'November', 'December', 'Year'])


            # Populate the utilization
            utilization_dict = calculate_utilization(df_samples, df_stats)
            util_instances = [Utilization(
                AssayID = record['AssayID'],
                MachineID = record['MachineID'],
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
                Year = record['Year']
            ) for record in utilization_dict]

            try:
                Utilization.objects.bulk_create(util_instances)
            except:
                Utilization.objects.bulk_update(util_instances, 
                fields=[ 'Assay', 'January', 'February', 'March', 'April', 'May', 'June',
                'July', 'August', 'September', 'October', 'November', 'December', 'Year'])


            # Populate the monthly stats
            monthly_stats = get_fullcapacity(df_samples, df_stats)
            mstats_instances = [monthlystats(
                AssayID = rec['AssayID'],
                MachineID = rec['MachineID'],
                MaxMonthlyhours = rec['MaxMonthlyhours'],
                MaxMonthlyRevenue = rec['MaxMonthlyRevenue'],
                MaxMonthSamples = rec['MaxMonthlySamples']
            ) for rec in monthly_stats]

            try:
                monthlystats.objects.bulk_create(mstats_instances)
            except:
                monthlystats.objects.bulk_update(mstats_instances, 
                fields=['MaxMonthlyhours', 'MaxMonthlyRevenue', 'MaxMonthSamples'])


            # Populate the missed revenue
            missed_dict = calculate_missedrevenue(revenue_dict, df_stats)

            Missed_instances = [MissedRevenue(
                AssayID = record['AssayID'],
                MachineID = record['MachineID'],
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
                Year = record['Year']
            ) for record in missed_dict]

            try:
                MissedRevenue.objects.bulk_create(Missed_instances)
            except:
                MissedRevenue.objects.bulk_update(Missed_instances, 
                fields=[ 'Assay', 'January', 'February', 'March', 'April', 'May', 'June',
                'July', 'August', 'September', 'October', 'November', 'December', 'Year'])
            messages.success(request, ("File uploaded sucessfully"))
        except:
            messages.error(request, ("Invalid file data. An error occured, please upload again"))
        obj.activated = True
        obj.save()
    return render(request, 'upload/upload.html', {'form': form})