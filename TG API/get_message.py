import requests

TOKEN = 'Вставьте свой токен сюда'
url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'

response = requests.get(url)
print(response.json())
