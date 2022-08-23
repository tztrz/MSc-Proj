#%%
#Import
import xarray as xr
import glob
import pandas as pd
#%%
dir_mean_temp = '/Users/Louisa/Desktop/MScProject/HADUKAnnual (1973-2020)/annual mean air temp'
#%%
 #loading all climate variable data from 1973 - 2020 into one dataframe, saving to csv for exploration
#filenames = glob.glob('/Users/Louisa/Desktop/MScProject/HADUKAnnual (1973-2020)/annual mean air temp/*.nc')
#clim_data_airtemp = xr.open_mfdataset(filenames)
#clim_data_df = clim_data.to_dataframe()
#clim_data_df.to_csv('/Users/Louisa/Desktop/climdata.csv') 

#%%
#print(clim_data_airtemp.variables.keys())
#39.19

#%%
# lat = clim_data_airtemp.variables['latitude'][:]
# lon = clim_data_airtemp.variables['longitude'][:]
# date = clim_data_airtemp.variables['']
# print(lat,lon)
# %%
site_indices = pd.read_csv('ukbms2020csv/ukbmssiteindices2020.csv',encoding='cp1252')
site_location_data = pd.read_csv('final_ukbmssitelocationdata2020.csv', encoding='cp1252')
#%%
site_indices_withcoords = pd.merge(site_indices,site_location_data[['Site Number','latitude','longitude']],on='Site Number',how='left')
# %%
