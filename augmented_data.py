import pandas as pd
import requests
import sqlalchemy
import os

df = pd.read_sql_table('Country','sqlite:///data/database.sqlite')
countries = df['name'].unique() #unique countries

public_token = "pk.eyJ1IjoibWVsbGlqb2FjbyIsImEiOiJjazNwNTc3a2YyOGp1M2RsZHNmcXIwdG5nIn0.hCauisNqiuFuVAnwiH7AQA"
private_token = os.environ['MAPBOX_PRIVATE_TOKEN'] # check this in the future

all_countries = {}
#there is a problem. MAPBOX do not consider countries inside UK as countries. It assigns the 'region' id.
for country in countries:
    query = "https://api.mapbox.com/geocoding/v5/mapbox.places/{}.json?types=country,region&access_token=".format(country) + public_token
    data = requests.get(query).json()
    all_countries[country] = data['features']
