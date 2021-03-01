# Locating and ploting the location of ISS

import pandas as pd
import plotly.express as px
import time

def get_coord(url):
    """ Get real-time coordinates of the ISS """

    # Read JSON from the URL
    coord= pd.read_json(url).drop('message', axis = 1)
    
    # Create new columns ['lat', 'long']
    coord['lat'] = coord.loc['latitude', 'iss_position']
    coord['long'] = coord.loc['longitude', 'iss_position']
    coord.reset_index(inplace=True)

    return coord

# API URL
url = 'http://api.open-notify.org/iss-now.json'

# Create an empty dataframe to store coordinates 
df = pd.DataFrame(columns = ['timestamp', 'lat','long'])

while True:

    # Get coordinates
    coord = get_coord(url)

    df = df.append({'timestamp':coord['timestamp'][0],
                    'lat':coord['lat'][0],
                    'long': coord['long'][0]},
                    ignore_index = True)

    fig = px.scatter_geo(df, lat = 'lat', lon = 'long')
    fig.show()

    time.sleep(20)
