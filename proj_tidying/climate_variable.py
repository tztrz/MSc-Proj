#%%
#Imports
import xarray as xr
import glob
import pandas as pd
#%%
dir_mean_temp = '/Users/Louisa/Desktop/MScProject/HADUKAnnual (1973-2020)/annual mean air temp'

# mean_annual_airtemp = pd.DataFrame()
# for filename in os.listdir(dir_mean_temp):
#     f = os.path.join(dir_mean_temp,filename)
#     if os.path.isfile(f):
#         #print(f)
#         file_open = xr.open_dataset(f)
#         file_open_todf = file_open.to_dataframe()
#         mean_annual_airtemp =mean_annual_airtemp.append(file_open_todf)

# mean_annual_airtemp.to_csv('meanannualairtemp.csv',encoding='utf-8')

#%%
 #loading all climate variable data from 1973 - 2020 into one dataframe, saving to csv for exploration
filenames = glob.glob('/Users/Louisa/Desktop/MScProject/HADUKAnnual (1973-2020)/*/*.nc')
clim_data = xr.open_mfdataset(filenames)
#clim_data_df = clim_data.to_dataframe()
#clim_data_df.to_csv('/Users/Louisa/Desktop/climdata.csv') 

#%%
print(clim_data.variables.keys())
#39.19

#%%
lat = clim_data.variables['latitude'][:]
lon = clim_data.variables['longitude'][:]
print(lat,lon)