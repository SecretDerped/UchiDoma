import csv

with open('data.csv', newline='') as file:
    data = csv.DictReader(file)
    print(data.fieldnames)
    for line in data:
        print(line['name'], line['height'])