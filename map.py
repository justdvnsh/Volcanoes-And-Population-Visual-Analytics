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

map = folium.Map([38.58, -99.09], zoom_start=6, tiles="mapbox Bright")

fg = folium.FeatureGroup(name="My Map")

for i,j,k in zip(lat, long, risk):
	fg.add_child(folium.Marker(location=[i,j], popup="Risk Factor: " + str(k), icon=folium.Icon(color=color_producer(k))))

map.add_child(fg)

map.save('map.html')
