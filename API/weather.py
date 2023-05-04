import requests

API_KEY = 'a5264c2c15fe7ddde568e96bfae26847'
WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather'
WEATHER_PARAMS = {
    'appid': API_KEY,
    'lat': '45.0448',
    'lon': '38.976',
    'units': 'metric',
    'lang': 'ru'
}

response = requests.get(WEATHER_URL, WEATHER_PARAMS)
json = response.json()
city = json['name']
weather = json['weather'][0]['description']
temp = json['main']['temp']
print(f'Погода в городе: {city}. {weather.capitalize()}, температура: {temp} °C.')
