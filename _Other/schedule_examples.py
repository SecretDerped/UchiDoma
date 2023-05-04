'''import datetime

date = datetime.datetime.now()
summer = datetime.date(2023, 6, 1)

stop_month = summer.month
month = date.month

weekdays = 0


while month != stop_month:
    if date.isoweekday() in [6, 7]:
        weekdays += 1
        month = date.month
        print(date.strftime('%d.%m.%Y'))
        print('Количество выходных:', weekdays)
    date += datetime.timedelta(days=1)'''




'''import datetime

weekdays = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']

date = datetime.datetime.strptime(input(), '%m %Y')

month = date.month
print(*weekdays, sep='\t', end='\t')
print()
print('\t'*date.weekday(), end='')
while month == date.month:
    print(date.day, end='\t')
    if date.isoweekday() == 7:
        print()
    date += datetime.timedelta(days=1)
print()'''

import datetime


total = 0
max_count = 3
count = int(input())
date = datetime.datetime.strptime(input(), '%d.%m.%Y')

while total < 4:
    if count < max_count:
        if date.isoweekday() in [6, 7] and date.day % 2 == 0:
            print(date.strftime('%d.%m.%Y'))
            total += 1
            count += 1
        date += datetime.timedelta(days=1)
    else:
        date += datetime.timedelta(date.year, date.month + 1, 1)
        count = 0



# import time:
