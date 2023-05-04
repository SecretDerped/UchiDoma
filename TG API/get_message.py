import requests

TOKEN = '5803675179:AAHtgKLhtwZC4caauw7aa3ilvDtgCd7v1J4'
url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'

response = requests.get(url)
print(response.json())
