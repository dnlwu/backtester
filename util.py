import pandas as pd

TIME_MAP = {'open': pd.Timedelta(hours=9,minutes=30), 'close': pd.Timedelta(hours=16)}

def compare_df_cols(df_a,df_b):
    df_a_cols = df_a.columns
    df_b_cols = df_b.columns
    
    common_cols = df_a_cols.intersection(df_b_cols)
    a_not_b = df_a_cols.difference(df_b_cols)

    return a_not_b