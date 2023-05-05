people = {1: ['Иван', {'фантастика', 'комикс', 'детектив', 'роман'}],
          2: ['Марина', {'комикс', 'фэнтези', 'детектив', 'комедия'}],
          3: ['Тим', {'фантастика', 'ужасы', 'детектив', 'драма'}],
          4: ['Никита', {'фэнтези', 'комедия', 'драма', 'комикс'}],
          5: ['Владимир', {'комикс', 'роман', 'комедия', 'драма'}]}


def reg():
    name = input('Введите имя: ')
    my_set = input(
        'Введи 4 книжных жанра через пробел: фантастика, детектив, комедия, роман, комикс, фэнтези, драма и т.п.').split()
    my_set = set(my_set)
    return my_set


def find_friend(my_set):
    for i in (people):
        result1 = my_set & (set(people[i][1]))
        result2 = my_set.union((set(people[i][1])))
        result = len(result1) / len(result2) * 100
        if round(result) > 15:
            print(people[i][0], round(result))
            print(people[i][1] - my_set)
    start()


def scrubble():
    points_ru = {1: 'АВЕИНОРСТ',
                 2: 'ДКЛМПУ',
                 3: 'БГЁЬЯ',
                 4: 'ЙЫ',
                 5: 'ЖЗХЦЧ',
                 8: 'ШЭЮ',
                 10: 'ФЩЪ'}
    text = input().upper()
    print(sum([k for i in text for k, v in points_ru.items() if i in v]))
    a = input('1-Сыграть еще раз 2-Главное меню')
    if a == '1':
        scrubble()
    elif a == '2':
        start()


def unic():
    n = set(input().lower())
    if len(n) > 15:
        print('Победа')
    else:
        print('Не хватило', 16 - (len(n)))
    a = input('1-Сыграть еще раз 2-Главное меню')
    if a == '1':
        unic()
    elif a == '2':
        start()


def anagram():
    a, b, c = input(), input(), input()
    a = {i: a.count(i) for i in a}
    b = {i: b.count(i) for i in b}
    c = {i: c.count(i) for i in c}
    print('Супер' if a == b == c else 'Не пытайся обмануть')
    a = input('1-Сыграть еще раз 2-Главное меню')
    if a == '1':
        anagram()
    elif a == '2':
        start()


def start():
    action = input('1-Найти друга 2-Играть 3-Выход')
    if action == '1':
        find_friend(a)
    if action == '2':
        game = input('1-Скрабл 2-Уникальные буквы 3-Анаграммы')
        if game == '1':
            scrubble()
        elif game == '2':
            unic()
        elif game == '3':
            anagram()
    if action == '3':
        print('Пока')


a = reg()
start()
