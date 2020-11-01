import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev= list(data["ELEV"])
type= list(data["TYPE"])

def color_producer(elevation):
    if elevation < 2000:
        return 'green'
    elif 2000 <= elevation < 3000:
        return 'yellow'
    else:
        return 'red'

map = folium.Map(location=[44.4197998,-101.7710037], zoom_start=4, tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el, tp in zip(lat,lon, elev, type):
    fg.add_child(folium.CircleMarker(location= [lt, ln], radius= 7, popup=str(el)+ " m." + str(tp),
    fill_color= color_producer(el), color='black', fill_opacity=0.7))

fh= folium.FeatureGroup(name="Countries")

fh.add_child(folium.GeoJson(data=open('world.json', 'r', encoding= 'utf-8-sig').read(),
style_function= lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
else 'yellow' if 10000000 <= x['properties']['POP2005'] < 50000000 else 'orange' if
50000000 <= x['properties']['POP2005'] < 100000000 else 'red' if 100000000 <= x['properties']['POP2005'] < 500000000 else 'black'}))


map.add_child(fg)
map.add_child(fh)
map.add_child(folium.LayerControl())

map.save("Map1.html")

