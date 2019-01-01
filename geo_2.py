import folium
from folium import vector_layers
import pandas as pd
import json


state_geo = json.load(open("us-states.json"))
state_data = pd.read_csv("us-unemployment.csv")

map = folium.Map(location=[48, -102], zoom_start=5)

map.choropleth(
    geo_data=state_geo,
    name='choropleth',
    data=state_data,
    columns=['State', 'Unemployment'],
    key_on='feature.id',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Unemployment Rate (%)'
)


folium.LayerControl().add_to(map)

map.save("map2.html")
