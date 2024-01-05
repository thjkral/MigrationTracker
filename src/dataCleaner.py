#!/usr/bin/env python3

def remove_nans(df):
    records_before = len(df.index)
    df_no_na = df.dropna(how='any')
    records_after = len(df_no_na.index)

    print(f'Removed {records_before - records_after} rows with NaN values')
    return df_no_na


def remove_duplicates(df):
    records_before = len(df.index)
    df_no_dup = df.drop_duplicates(keep='first')
    records_after = len(df_no_dup.index)

    print(f'Removed {records_before - records_after} duplicate rows')
    return df_no_dup


def full_clean(df):
    df = remove_nans(df)
    df = remove_duplicates(df)
