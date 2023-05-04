import re
import sys


pattern = r'[-_\.\,!*\s]+'
string = 'привет   дом-кот__время.место,дверь***.дерево вечер_--рука!!поэт*два'
print(*re.split(pattern, string), sep ='\n')


'''pattern = r'[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}'
for line in sys.stdin:
    line = line.strip()
    if re.match(pattern, line):
        print(True)
    else:
        print(False)'''



'''
pattern1 = r'\d\d\.\d\d'

string = '01.12 должно было произойти что-то, но произойдет 02.12.2023'

match1 = re.search(pattern1, string)
match2 = re.search(pattern2, string)
print(match1)  # <re.Match object; span=(0, 5), match='01.12'>
print(match2)  # <re.Match object; span=(50, 60), match='02.12.2023'>

match3 = re.match(pattern1, string)
match4 = re.match(pattern2, string)
print(match3)  # <re.Match object; span=(0, 5), match='01.12'>
print(match4)  # None

match = re.findall(pattern1, string)
print(match)  # ['01.12', '02.12']

result = re.split(pattern1, string)
print(result)  # ['', ' должно было произойти что-то, но произойдет ', '.2023']

new_string = re.sub(pattern1, '-удалено-', string)
print(new_string)  # -удалено- должно было произойти что-то, но произойдет -удалено-.2023
match1 = re.search(pattern1, string, re.IGNORECASE)
'''
