import requests

TOKEN = '5803675179:AAHtgKLhtwZC4caauw7aa3ilvDtgCd7v1J4'
url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
params = {'chat_id': '1945461539',
          'text': 'Hello!'}

response = requests.get(url, params)
print(response.json())
