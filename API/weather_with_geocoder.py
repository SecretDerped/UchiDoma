import requests

API_KEY = 'a5264c2c15fe7ddde568e96bfae26847'
WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather'
GEOCODER_URL = 'http://api.openweathermap.org/geo/1.0/direct'
WEATHER_PARAMS = {
    'appid': API_KEY,
    'units': 'metric',
    'lang': 'ru'
}

GEOCODER_PARAMS = {
    'appid': API_KEY
}


def get_city_coords(city):
    GEOCODER_PARAMS['q'] = city
    json = requests.get(GEOCODER_URL, GEOCODER_PARAMS).json()
    lat, lon = json[0]['lat'], json[0]['lon']
    return lat, lon


def get_weather(lat, lon):
    WEATHER_PARAMS['lat'], WEATHER_PARAMS['lon'] = lat, lon
    json = requests.get(WEATHER_URL, WEATHER_PARAMS).json()
    city = json['name']
    description = json['weather'][0]['description']
    temp = json['main']['temp']
    return f'Погода в городе: {city}. {description.capitalize()}, температура: {temp} °C.'


city = input()
lat, lon = get_city_coords(city)
result = get_weather(lat, lon)
print(result)
