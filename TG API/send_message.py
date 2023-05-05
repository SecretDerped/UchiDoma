import requests

TOKEN = 'Вставьте свой токен сюда'

url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
params = {'chat_id': '1945461539',
          'text': 'Hello!'}

response = requests.get(url, params)
print(response.json())
