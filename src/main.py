#!/usr/bin/env python3
"""
Main Python script
"""

# import modules
import pandas
import matplotlib.pyplot as plt
import descartes
import geopandas as gpd
from shapely.geometry import Point, Polygon
import json

# import Python scripts
import dataLoader
import dataCleaner

# load config
with open('/etc/migrationconfig/config.json') as f:
    config = json.load(f)

# STEP 1: load data
data = dataLoader.get_data_from_file(config['datafile'])

# STEP 2: validate and clean data
df = data[['occurrenceID', 'verbatimScientificName', 'countryCode',
           'stateProvince', 'individualCount', 'eventDate', 'decimalLatitude', 'decimalLongitude']]

df = dataCleaner.full_clean(df)

# STEP 3: save data
# only implement if datasets get too large

# STEP 4: visualise data
shapefile = gpd.read_file(config['shapefile'])
crs = {'init': 'epsg:4326'}

print('Bye!')
