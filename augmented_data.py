import pandas as pd
import requests
import sqlalchemy
import os

df = pd.read_sql_table('Country','sqlite:///data/database.sqlite')
countries = df['name'].unique() # unique countries

public_token = "pk.eyJ1IjoibWVsbGlqb2FjbyIsImEiOiJjazNwNTc3a2YyOGp1M2RsZHNmcXIwdG5nIn0.hCauisNqiuFuVAnwiH7AQA"
private_token = os.environ['MAPBOX_PRIVATE_TOKEN'] # check this in the future

all_countries = {}
# there is a problem. MAPBOX do not consider countries inside UK as countries. It assigns the 'region' id.

for country in countries:
    query = "https://api.mapbox.com/geocoding/v5/mapbox.places/{}.json?types=country,region&access_token=".format(country) + private_token
    data = requests.get(query).json()
    all_countries[country] = data['features'] # data from mapbox for every country in our table

#bbox =  minLon,minLat,maxLon,maxLat
df['lat'] = None
df['long'] = None
df['country_id'] = None

# Quick way to add all the values in a DF format.
for country in countries:
    df.loc[df['name'] == country, 'country_id'] = all_countries[country][0]['id']
    df.loc[df['name'] == country, 'lat'] = str(all_countries[country][0]['bbox'][1::2])
    df.loc[df['name'] == country, 'long'] = str(all_countries[country][0]['bbox'][0::2])

#Creating SQL table
engine = sqlalchemy.create_engine('sqlite:///data/database.sqlite')
conn = engine.connect()
conn.execute('DROP TABLE IF EXISTS  latlong;')
# I need to check what is the format for the lat and long columns. I am assuming text now just to run a test
conn.execute('''
    create table latlong (
        id TEXT PRIMARY KEY,
        country_id TEXT,  
        country_name TEXT, 
        lat TEXT,
        long TEXT); 
''')
# Adding the values to the SQL table
for row in list(df.index):
    query = f'("{df.loc[row,"id"]}", "{df.loc[row,"country_id"]}",' \
            f' "{df.loc[row,"name"]}", "{df.loc[row,"lat"]}", "{df.loc[row,"long"]}")'
    conn.execute( 'INSERT INTO latlong (id, country_id, country_name, lat, long) VALUES ' + query)

conn.close()