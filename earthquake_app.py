import requests


url = 'https://earthquake.usgs.gov/fdsnws/event/1/query'
starttime = input('Enter the start time: ')
endtime = input('Enter the end time: ')
latitude = input('Enter the latitude: ')
longitude = input('Enter the longitude: ')
maxradiuskm = input('Enter the max radius in km: ')
minmagnitude = input('Enter the min magnitude: ')
headers = {'Access': 'application/json'}
data_request = {
	'url': url,
	'params': {
	'format': 'geojson',
	'starttime': starttime,
	'endtime': endtime,
	'latitude': latitude,
	'longitude': longitude,
	'maxradiuskm': maxradiuskm,
	'minmagnitude': minmagnitude,
	},
	'headers': headers,
}



response = requests.get(**data_request)
if response.status_code == 200:
	data = response.json()
	features = data.get('features', [])
	if features:
		for i, f in enumerate(features, start=1):
			output = f'{i}) Place: {f.get("properties").get("place")}. Magnitude: {f.get("properties").get("mag")}'
			print(output)

else:
	print('Что-то пошло не так')