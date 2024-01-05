#!/usr/bin/env python3
"""
Get the requested data from its original source
"""

import pandas


def get_data_from_file(filepath):
    """
    Read the data from a single tab-delimited file
    :param filepath: path to the file
    :return: Pandas dataframe
    """
    df = pandas.read_csv(filepath,
                         header=0,
                         sep='\t',
                         low_memory=False,
                         index_col=0)
    return df


if __name__ == '__main__':
    get_data_from_file('/home/tom/ResearchData/migration/pestvogel.csv')
