# Purpose: Analysis on internet in specific areas of Florida
# Date Created: 10/21/2022
# Date Last Updated: 10/21/2022
#
########################################################################################################################
# Imports
import pandas as pd

########################################################################################################################
# Read and prepare fl_internet Excel Sheets as DataFrames

# Path to Excel Workbook
fl_internet_path = f"C:/Users/viole/OneDrive/Documents/real-estate/florida_internet.xlsx"

# Read sheet with internet Mbps by county
# This list contains counties of interest based on location and internet speed only
fl_county_internet_df = pd.read_excel(fl_internet_path, sheet_name='fl_county_internet')

# Set Index of fl_county_internet_df to County
fl_county_internet_df.set_index('county')

# Exploring fl_county_internet_df DataFrame
# print(fl_county_internet_df.head())
# print(fl_county_internet_df.columns)
# print(fl_county_internet_df.describe())

# Read sheet with internet Mbps by city
#
fl_city_internet_df = pd.read_excel(fl_internet_path, sheet_name='fl_city_internet')

# Set Index of fl_city_internet_df to City
# Includes all cities for which data is available
fl_city_internet_df.set_index('city')

# Explore fl_city_internet_df
# print(fl_city_internet_df.head())
# print(fl_city_internet_df.columns)
# print(fl_city_internet_df.describe())

# Read sheet with Area, County, and City mapping
# Includes all FL cities
# NaN for rows not in a desired location
# Non-desired locations are locations not in fl_county_internet_df
fl_location_map_df = pd.read_excel(fl_internet_path, sheet_name = 'fl_cities')

# Set Index of fl_location_map_df to City
fl_location_map_df.set_index('city')

# Explore fl_location_map_df
# print(fl_location_map_df.head())
# print(fl_location_map_df.columns)
# print(fl_location_map_df.describe())
#
########################################################################################################################
