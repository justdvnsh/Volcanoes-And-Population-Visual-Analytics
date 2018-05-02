import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")

lat = list(data["LAT"])
long = list(data["LON"])
elev = list(data["ELEV"])

map = folium.Map([38.58, -99.09], zoom_start=6, tiles="mapbox Bright")

fg = folium.FeatureGroup(name="My Map")

for i,j,k in zip(lat, long, elev):
	fg.add_child(folium.Marker(location=[i,j], popup="Elevation form the sea: " + str(k) + ' m', icon=folium.Icon(color="green")))

map.add_child(fg)

map.save('map.html')
