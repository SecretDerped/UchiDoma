import datetime
from flask import Flask


app = Flask(__name__)


def get_date_or_time(mode):
    dt = datetime.datetime.now()
    if mode == 'date':
        return f'<h1>Текущая дата: {dt.strftime("%d.%m.%Y")}</h1>'
    if mode == 'time':
        return f'<h1>Текущее время: {dt.strftime("%H:%M")}</h1>'
    else:
        return f'<h1>URL должен кончаться на time или date</h1>'


app.add_url_rule('/<mode>', 'datetime', get_date_or_time)

if __name__ == '__main__':
    app.run()
    