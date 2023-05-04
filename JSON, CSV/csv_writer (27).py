import csv

names = ['name', 'height', 'mass']
rows = [
    {'name': 'Luke Skywalker', 'height': '172', 'mass': '77'},
    {'name': 'C-3PO', 'height': '167', 'mass': '75'},
    {'name': 'R2-D2', 'height': '96', 'mass': '32'},
    {'name': 'Darth Vader', 'height': '202', 'mass': '136'},
    {'name': 'Leia Organa', 'height': '150', 'mass': '49'},
    {'name': 'Yoda', 'height': '66', 'mass': '17'}
]

with open('data_out.csv', 'w', newline='') as file:
    data = csv.DictWriter(file, fieldnames=names)
    data.writeheader()
    data.writerows(rows)
