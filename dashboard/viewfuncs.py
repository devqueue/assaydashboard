
def index_context(YEAR, MONTH, MACHINE, samples_df, revenue_df):
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
    return context


def sample_context(YEAR, MONTH, samples_df, monthlystats_df):
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

    return context 

def util_context(YEAR, MONTH, util_df, monthlystats_df):
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
    return context

def revenue_context(YEAR, MONTH, revenue_df, monthlystats_df):
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
    return context