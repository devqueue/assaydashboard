import pandas as pd
import numpy as np


def create_df(csvfilepath):
    df = pd.read_csv(csvfilepath)
    df = df.replace(np.nan, 0)
    records = df.to_dict('records')
    return records


def get_yearfromindex(index):
    _, yearsuf = index[0].split('_')
    year = '20' + yearsuf

    return year


def normalize_index(index):
    flat_index = []
    for i in index:
        assay, _ = i.split('_')
        flat_index.append(assay)
    return flat_index


def create_stats():
    df_stats = pd.DataFrame({
    "Price": [125,275,400,500,400,350],
    "Run time": [2, 45, 120, 20, 20, 1],
    "Full capacity": [6240, 6240, 6240, 6240, 6240, 6240],
    "Maintenance": [520, 520, 520, 520, 520, 520],
    "MachineID": ["FI-MSMS", "GC-MS", "Amino acid analyzer", "LC-MSMS-1" ,"LC-MSMS-2" , "Spectrophotometer"],
    "AssayID": ["SICKPANEL", "OA", "AAA", "VLCFA", "MMA", "SERUM"]
    }, index=["SICKPANEL", "OA", "AAA", "VLCFA", "MMA", "SERUM"])

    records = df_stats.to_dict('records')
    return records


def calculate_revenue(df_year_dict, stats_dict):
    df_year = pd.DataFrame(df_year_dict)
    df_year.index = df_year['AssayID']
    df_year.drop(['AssayID'], inplace=True, axis=1)

    df_stats = pd.DataFrame(stats_dict)
    
    df_only_sample = df_year.loc[:, ~((df_year.columns == 'Assay') | (df_year.columns == 'Year') | (df_year.columns == 'MachineID'))]
    df_revenue = pd.DataFrame(df_only_sample.values*(df_stats.Price.values).reshape(6,1), columns=df_only_sample.columns, index=df_only_sample.index)
    df_revenue.insert(loc=0, column='Assay', value=df_year['Assay'])
    df_revenue['Year'] = df_year['Year']
    df_revenue['AssayID'] = df_year.index
    df_revenue['MachineID'] = df_year['MachineID']

    records = df_revenue.to_dict('records')
    return records



def calculate_utilization(df_year_dict, stats_dict):
    df_year = pd.DataFrame(df_year_dict)
    df_year.index = df_year['AssayID']
    df_year.drop(['AssayID'], inplace=True, axis=1)

    df_stats = pd.DataFrame(stats_dict)

    df_only_sample = df_year.loc[:, ~((df_year.columns == 'Assay') | (df_year.columns == 'Year') | (df_year.columns == 'MachineID'))]
    runtime = (df_stats['Run time'].values).reshape(6,1) / np.full(shape=(6,1), fill_value=60) 
    formula = ((df_only_sample.values * runtime))

    df_util = pd.DataFrame(formula, columns=df_only_sample.columns, index=df_only_sample.index)
    df_util = df_util.round(2)
    df_util.insert(loc=0, column='Assay', value=df_year['Assay'])
    df_util['Year'] = df_year['Year']
    df_util['AssayID'] = df_year.index
    df_util['MachineID'] = df_year['MachineID']

    record = df_util.to_dict('records')
    return record


def get_fullcapacity(df_year_dict, stats_dict):
    df_year = pd.DataFrame(df_year_dict)
    df_stats = pd.DataFrame(stats_dict)

    fullcap = ((df_stats['Full capacity'].values).reshape(6,1) - df_stats["Maintenance"].values.reshape(6,1)) / np.full(shape=(6,1),fill_value=12)
    runtime = (df_stats['Run time'].values).reshape(6,1) / np.full(shape=(6,1),fill_value=60)
    price = (df_stats['Price'].values).reshape(6,1)

    fullcap_samples = fullcap / runtime

    fullrev = fullcap_samples * price

    df_fullcap = pd.DataFrame(fullcap, columns=['MaxMonthlyhours'])
    df_fullcap['MaxMonthlySamples'] = fullcap_samples
    df_fullcap['MaxMonthlyRevenue'] = fullrev
    df_fullcap['AssayID'] = normalize_index(df_year['AssayID'])
    df_fullcap['MachineID'] = df_year['MachineID']

    records  = df_fullcap.to_dict('records')

    return records


def calculate_missedrevenue(df_revenue_dict, stats_dict):
    df_revenue = pd.DataFrame(df_revenue_dict)
    df_stats = pd.DataFrame(stats_dict)

    df_only_revenue = df_revenue.loc[:, ~((df_revenue.columns == 'Assay') | (df_revenue.columns == 'Year') | (df_revenue.columns == 'AssayID') | (df_revenue.columns == 'MachineID') )]

    actual_revenue = df_only_revenue.values

    fullcap = (df_stats['Full capacity'].values).reshape(6,1) / np.full(shape=(6,1),fill_value=12)
    fullcap = (np.repeat(fullcap[:, :, np.newaxis], 12, axis=2)).reshape(6, 12)

    runtime = (df_stats['Run time'].values).reshape(6,1) / np.full(shape=(6,1),fill_value=60)
    runtime = (np.repeat(runtime[:, :, np.newaxis], 12, axis=2)).reshape(6, 12)

    price = (df_stats['Price'].values).reshape(6,1)
    price = (np.repeat(price[:, :, np.newaxis], 12, axis=2)).reshape(6, 12)

    fullcap_samples = fullcap / runtime
    full_revenue = fullcap_samples * price

    missedrev = full_revenue - actual_revenue
    
    df_missedrev = pd.DataFrame(missedrev, columns=df_only_revenue.columns)
    df_missedrev['AssayID'] = df_revenue['AssayID']
    df_missedrev['Assay'] = df_revenue['Assay']
    df_missedrev['Year'] = df_revenue['Year']
    df_missedrev['MachineID'] = df_revenue['MachineID']

    record = df_missedrev.to_dict('records')
    return record