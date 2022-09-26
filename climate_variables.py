#%%
#Imports
import xarray as xr
import glob
import pandas as pd
#%%
#Loading all climate variable data from 1973 - 2020 into one dataframe, saving to csv for exploration

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
site_indices_withcoords = pd.merge(site_indices,site_location_data[['Site Number','Easting','Northing']],on='Site Number',how='left')
site_indices_withcoords.dropna(inplace=True)
site_indices_withcoords['YEAR'] = site_indices_withcoords['YEAR'].astype(str)

#drop rows where site index is -2 (indicating that not enough data was collected to calculate sight index
site_indices_withcoords.drop(site_indices_withcoords.loc[site_indices_withcoords['SITE INDEX']==-2].index, inplace=True)
#print(len(site_indices))
#print(len(site_indices_withcoords))
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

# %%
#inital attempts to convert latitude and longitude values to transverse mercator projections before realising that os national grid easting and northing was already a transverse mercator projection.

#data_crs = ccrs.TransverseMercator(central_longitude=-2.0, central_latitude=49.0, false_easting=400000, false_northing= -100000,scale_factor=0.9996012717)
#x,y = data_crs.transform_point(51.793949,-2.1550988, src_crs=ccrs.PlateCarree())
#print(x,y)

# x,y = 521000.0,281000
# dat = '1997'
# example = sunshine_dat.sel(time = dat, projection_x_coordinate=x,projection_y_coordinate=y,method='nearest')
# print(example['time'].values,example['sun'].values)
# print(example['latitude'].values, example['longitude'].values)

# %%
def get_value(netcdf, date, x, y, var_name):
    '''Retrives the value of a specified variable from HADUK netcdf dataset nearest to desired point'''
    dat = netcdf.sel(time = date, projection_x_coordinate=x,projection_y_coordinate=y,method='nearest')
    value1 = dat[var_name].values
    return value1
#%%
#matching species indices with corresponding climatic data using apply and get_value function
#nb this ran for approx three hours
site_indices_withcoords['sun'] = site_indices_withcoords.apply(lambda row: get_value(sunshine_dat, row['YEAR'], row['Easting'], row['Northing'], 'sun'), axis =1)
site_indices_withcoords['average temp'] = site_indices_withcoords.apply(lambda row: get_value(airtemp_dat, row['YEAR'], row['Easting'], row['Northing'], 'tas'), axis =1)
site_indices_withcoords['rainfall'] = site_indices_withcoords.apply(lambda row: get_value(rainfall_dat, row['YEAR'], row['Easting'], row['Northing'], 'rainfall'), axis =1)
site_indices_withcoords['relative humidity'] = site_indices_withcoords.apply(lambda row: get_value(humidity_dat, row['YEAR'], row['Easting'], row['Northing'], 'hurs'), axis =1)

#saving to csv so not necessary to run again
site_indices_withcoords.to_csv('/Users/Louisa/Desktop/site_climate.csv')                                                                                               