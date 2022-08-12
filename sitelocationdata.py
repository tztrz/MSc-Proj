from OSGridConverter import grid2latlong
import pandas as pd
site_loc = pd.read_csv('ukbms2020csv/ukbmssitelocationdata2020.csv', encoding='cp1252')

def get_lat(df):
    l = grid2latlong(df['Gridreference'])
    return l.latitude

def get_long(df): 
    l = grid2latlong(df['Gridreference'])
    return l.longitude

site_loc['latitude'] = site_loc.apply(get_lat(site_loc), axis=1)
print(site_loc.head())