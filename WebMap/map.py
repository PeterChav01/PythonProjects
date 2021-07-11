import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation <= 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[19.24082756088302, -103.72444548089366], zoom_start=9, tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name="My map")
for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location= [lt, ln], radius = 6, popup=folium.Popup(str(el),parse_html=True), 
    fill_color=color_producer(el), color = 'grey', fill_opacity=0.7, fill = True ))


fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), 
style_function= lambda x: {'fillColor':'yellow' if x['properties']['POP2005'] < 1000000 
else 'orange' if 1000000 <= x['properties']['POP2005'] < 2000000 else 'red'}))

map.add_child(fg)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")