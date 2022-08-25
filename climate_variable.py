#%%
#Imports
import xarray as xr
import glob
import pandas as pd
#%%
'''Loading all climate variable data from 1973 - 2020 into one dataframe, saving to csv for exploration'''
#filenames = glob.glob('/Users/Louisa/Desktop/MScProject/HADUKAnnual (1973-2020)/annual mean air temp/*.nc')
#clim_data_airtemp = xr.open_mfdataset(filenames)
#clim_data_df = clim_data.to_dataframe()
#clim_data_df.to_csv('/Users/Louisa/Desktop/climdata.csv') 

# %%
#Loading site_indices and completed location data (see  /Missing Site Location Data/sitelocationdata.py)
site_indices = pd.read_csv('ukbms2020csv/ukbmssiteindices2020.csv',encoding='cp1252')
site_location_data = pd.read_csv('final_ukbmssitelocationdata2020.csv', encoding='cp1252')
#%%
#Combining all site indices records with applicable coordinates, dropping records without associated location data
site_indices_withcoords = pd.merge(site_indices,site_location_data[['Site Number','latitude','longitude']],on='Site Number',how='left')
site_indices_withcoords.dropna(inplace=True)
# %%
#Loading climatic variable data for years 1973 - 2020
airtemp_filenames = glob.glob('/Users/Louisa/Desktop/MScProject/HADUKAnnual (1973-2020)/annual mean air temp/*.nc')
rainfall_filenames = glob.glob('/Users/Louisa/Desktop/MScProject/HADUKAnnual (1973-2020)/annual rainfall/*.nc')
humidity_filenames = glob.glob('/Users/Louisa/Desktop/MScProject/HADUKAnnual (1973-2020)/relative humidity/*.nc')
sunshine_filenames = glob.glob('/Users/Louisa/Desktop/MScProject/HADUKAnnual (1973-2020)/sunshine hours/*.nc')
airtemp_dat = xr.open_mfdataset(airtemp_filenames)
rainfall_dat = xr.open_mfdataset(rainfall_filenames)
humidity_dat = xr.open_mfdataset(humidity_filenames)
sunshine_dat = xr.open_mfdataset(sunshine_filenames)
#%%