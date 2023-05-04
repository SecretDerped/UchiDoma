import csv

names = ['name', 'height', 'mass', 'hair_color', 'skin_color']
rows = [
    ['Luke Skywalker', '172', '77', 'blond', 'fair'],
    ['C-3PO', '167', '75', 'NA', 'gold'],
    ['R2-D2', '96', '32', 'NA', 'white, blue'],
    ['Darth Vader', '202', '136', 'none', 'white'],
    ['Leia Organa', '150', '49', 'brown', 'light'],
    ['Yoda', '66', '17', 'white', 'green']
]

with open('data.csv', 'w', newline='') as file:
    data = csv.writer(file)
    data.writerow(names)
    data.writerows(rows)
