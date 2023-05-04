import requests
import random
from flask import Flask


app = Flask(__name__)


def get_data():
    data = []
    with open('data.txt', encoding='utf-8') as file:
        for line in file:
            data.append(line.strip())
    return data


def get_course():
    response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    result = ''
    print(response['Valute'])
    for i, data in response['Valute'].items():
        result += f'{data["Nominal"]} {data["Name"]} стоит {data["Value"]} руб.<br>'
    return result


def get_fibonacci_numbers(n):
    numbers = [1, 1]
    for i in range(2, n):
        numbers.append(numbers[i - 1] + numbers[i - 2])
    return numbers


@app.route("/")
@app.route("/home")
def index():
    return "Главная страница"


@app.route("/news")
def news():
    return "Страница с новостями"


@app.route("/about")
def about():
    return "Сайт с новостями"


@app.route("/fibonacci")
def fibonacci():
    return ' '.join([str(s) for s in get_fibonacci_numbers(n)])


@app.route("/money")
def money():
    return get_course()


@app.route("/random")
def quote():
    data = get_data()
    return random.choice(data)


if __name__ == '__main__':
    n = 100
    app.run()
