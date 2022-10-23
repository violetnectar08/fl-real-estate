# Purpose: Analysis on internet in specific areas of Florida
# Date Created: 10/21/2022
# Date Last Updated: 10/21/2022
#
# Internet Speeds pulled from https://broadbandnow.com/Florida
########################################################################################################################
# Imports
import pandas as pd

########################################################################################################################
# Read and prepare fl_internet Excel Sheets as DataFrames

# Path to Excel Workbook
fl_internet_path = f"C:/Users/viole/OneDrive/Documents/real-estate/florida_internet.xlsx"

# Read sheet with internet Mbps by county
# This df contains counties of interest based on location and internet speed only
fl_county_internet_df = pd.read_excel(fl_internet_path, sheet_name='fl_county_internet')
fl_county_internet_df.set_index('county', inplace=True) #inplace=True creates new (updated) df

# Read sheet with internet Mbps by city
# This df includes all cities for which data is available (not just in counties in fl_county_internet_df)
fl_city_internet_df = pd.read_excel(fl_internet_path, sheet_name='fl_city_internet')
fl_city_internet_df.set_index('city', inplace=True)

# Read sheet with Area, County, and City mapping
# Includes all FL cities
fl_location_map_df = pd.read_excel(fl_internet_path, sheet_name='fl_cities')
fl_location_map_df.set_index('city', inplace=True)
# Drop rows with missing data in area column (non-desired areas are NaN)
fl_location_map_df.dropna(subset=['area'], inplace=True)

# Limit cities in fl_location_map_df to cities in counties from fl_county_internet_df
fl_location_map_df = fl_location_map_df.loc[fl_location_map_df.county.isin(list(fl_county_internet_df.index))]















# Column provider_count in fl_city_internet_df is a string with format "<int> providers"
# We want an integer only with no text
# fl_city_internet_df['provider_count'].str.extract('(\d+)')
# map takes the function(lambda) and creates formula for each item in list (argument 2)
# list forces the computation of each of the formulas created by the map function
fl_city_internet_df['provider_count'] = list(map(lambda x: int(x.split(" providers")[0]),
                                                 fl_city_internet_df['provider_count'].to_list()
                                                 ))

########################################################################################################################
