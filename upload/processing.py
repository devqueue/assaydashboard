import pandas as pd
import numpy as np


def read_df(csvfilepath):
    df = pd.read_csv(csvfilepath)
    records = df.to_dict('records')
    print(records)
    return records

