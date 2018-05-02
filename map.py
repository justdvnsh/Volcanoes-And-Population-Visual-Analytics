import folium
import pandas

data = pandas.read_csv("volcano.csv")

lat = list(data["Latitude"])
long = list(data["Longitude"])
risk = list(data["risk"])

def color_producer(risk):
	if risk == 1 or risk == 2:
		return 'orange'
	elif risk >= 3:
		return 'red'
	else:
		return 'green'

map = folium.Map([38.58, -99.09], zoom_start=6, tiles="Mapbox Bright")

fgv = folium.FeatureGroup(name="Volcanoes")

for i,j,k in zip(lat, long, risk):
	fgv.add_child(folium.Marker(location=[i,j], popup="Risk Factor: " + str(k), icon=folium.Icon(color=color_producer(k))))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())

map.save('map.html')
