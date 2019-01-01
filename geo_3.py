from branca.utilities import split_six
from folium import vector_layers
import folium
import json
import pandas as pd
from folium.features import Choropleth


state_geo = json.load(open("us-states.json"))
state_data = pd.read_csv("us-unemployment.csv")
threshold_scale = split_six(state_data['Unemployment'])
#  for some reason it does return max range
#  adding manually
threshold_scale.append(11.0)

map = folium.Map(location=[48, -102], zoom_start=5)


Choropleth(
    geo_data=state_geo,
    data=state_data,
    columns=['State', 'Unemployment'],
    key_on='feature.id',
    fill_color='Spectral',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Unemployment Rate (%)',
    threshold_scale=threshold_scale
).add_to(map)


map.save("map3.html")
