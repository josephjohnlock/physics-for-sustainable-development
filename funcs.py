import pandas as pd
import numpy as np

def threshold_filter(
    df: pd.DataFrame, 
    column: str, 
    threshold: float, 
    timestamp_col: str = 'Timestamp', 
) -> tuple[pd.DataFrame, pd.DataFrame]:

    '''Remove rows where the specified column exceeds the threshold.'''

    out = df.copy()


    # if not pd.api.types.is_datetime64_any_dtype(out[timestamp_col]):
    #     out[timestamp_col] = out[timestamp_col].str[:19]
    #     out[timestamp_col] = pd.to_datetime(out[timestamp_col])

    bad = out[column] > threshold

    filtered = out.loc[~bad].copy()
    removed = out.loc[bad].copy()
    
    return filtered, removed


def low_filter(
    df: pd.DataFrame, 
    column: str, 
    threshold: float, 
    timestamp_col: str = 'Timestamp', 
) -> tuple[pd.DataFrame, pd.DataFrame]:

    '''Remove rows where the specified column is below the threshold.'''

    out = df.copy()


    # if not pd.api.types.is_datetime64_any_dtype(out[timestamp_col]):
    #     out[timestamp_col] = out[timestamp_col].str[:19]
    #     out[timestamp_col] = pd.to_datetime(out[timestamp_col])

    bad = out[column] < threshold

    filtered = out.loc[~bad].copy()
    removed = out.loc[bad].copy()

    return filtered, removed