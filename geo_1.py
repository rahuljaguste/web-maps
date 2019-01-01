import folium
from folium.plugins import MarkerCluster
import pandas as pd


data = pd.read_csv("Volcanoes_USA.txt")
lat = data["LAT"]
lon = data["LON"]
elevation = data["ELEV"]

def color_change(elevation):
    if(elevation<1000):
        return('green')
    elif (1000 <= elevation < 3000):
        return('orange')
    else:
        return ('red')


map = folium.Map(location=[37.296933, -121.9574983],
                 zoom_start=5, tiles="Mapbox bright")

#  Dark mode
#  map = folium.Map(location=[37.296933, -121.9574983],
#                 zoom_start=5, tiles="CartoDB dark_matter")

#Create Cluster
marker_cluster = MarkerCluster().add_to(map)

#Plot Markers
for lat, lon, elevation in zip(lat, lon, elevation):
    folium.Marker(location=[lat, lon], popup=str(elevation), icon=folium.Icon(
        color=color_change(elevation))).add_to(marker_cluster)


""" for lat,lon,elevation in zip(lat,lon,elevation):
        folium.CircleMarker(location=[lat, lon], popup=str(
            elevation)+" m", fill_color=color_change(elevation), color="gray", fill_opacity=0.9).add_to(marker_cluster)
 """


#Save the map
map.save("map1.html")
# map.render()

