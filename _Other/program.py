import argparse

op = {'add': lambda a, b: a + b,
      'sub': lambda a, b: a - b,
      'mul': lambda a, b: a * b,
      'div': lambda a, b: a / b}

parser = argparse.ArgumentParser()
parser.add_argument('a', type=int)
parser.add_argument('b', type=int)
parser.add_argument(
    '-o',
    choices=['add', 'sub', 'mul', 'div'],
    default='add'
)
args = parser.parse_args()

try:
    print(op[args.o](args.a, args.b))
except ZeroDivisionError:
    print('Ошибка')