from OSGridConverter import grid2latlong
import pandas as pd
site_loc = pd.read_csv('ukbms2020csv/ukbmssitelocationdata2020.csv', encoding='cp1252')

# def get_lat(df):
#     l = grid2latlong(df['Gridreference'])
#     return l.latitude

# def get_long(df): 
#     l = grid2latlong(df['Gridreference'])
#     return l.longitude

# site_loc['latitude'] = site_loc.apply(get_lat(site_loc), axis=1)
# print(site_loc.head())

grid_refs = site_loc['Gridreference'].tolist()
print(str(grid_refs)

# latitude = []
# for i in grid_refs:
#     l = grid2latlong(i)
#     latitude.append(l.latitude)

# longitude = []
# for i in grid_refs:
#     l = grid2latlong(i)
#     latitude.append(l.longitude)

# site_loc['latitude'] = latitude
# site_loc['longtitude'] = longitude
# print(site_loc.head())



