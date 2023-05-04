import json
import csv

data = json.load(open('rate.json', encoding='utf-8'))['Valute']
valutes = sorted([{'Name': data[i]['Name'], 'CharCode': data[i]['CharCode']}
                  for i in data], key=lambda dictionary: dictionary['CharCode'])

names = ['CharCode', 'Name']
with open('FILE.csv', 'w', encoding='utf-8', newline='') as f:
    d = csv.DictWriter(f, fieldnames=names)
    d.writeheader()
    d.writerows(valutes)
