from math import nan
from pickle import TRUE
from typing import no_type_check_decorator
from OSGridConverter import grid2latlong
import pandas as pd
site_loc = pd.read_csv('updated_sitelocation.csv', encoding='cp1252')

#after using gridreference finder.com there were missing values, compiled into list below
ist = []
for i in site_loc.index:
    if pd.isna(site_loc['latitude'][i]):
        ist.append ([site_loc['Site Number'][i],site_loc['Gridreference'][i],site_loc['Easting'][i],site_loc['Northing'][i]])

missing_gridref = pd.DataFrame(ist, columns = ['Site Number','Gridreference','Easting','Northing'])        

#print(missing_gridref.to_csv())
site_loc.drop(['updatedgridref'], axis=1,inplace=True)

#loading missing gridreferences dropping unessecary columns
missing_site_loc = pd.read_csv('missing_sitelocationdata.csv',encoding='cp1252')
missing_site_loc.drop(['ind','updatedgridref'], axis =1, inplace=True)
print(missing_site_loc.head())