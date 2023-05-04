from flask import Flask


app = Flask(__name__)


@app.route("/<int:a>/<string:operation>/<int:b>")
def det_calc(a, operation, b):
    if operation == '+':
        return f'<h1>{a + b}</h1>'
    elif operation == '-':
        return f'<h1>{a - b}</h1>'
    elif operation == '*':
        return f'<h1>{a * b}</h1>'
    elif operation == ':':
        return f'<h1>{a / b}</h1>' if b != 0 else '<h1>Ошибка</h1>'
    else:
        return '<h1>Калькулятор принимает запрос в формате:  /[число]/[знак]/[число]</h1>'


if __name__ == '__main__':
    app.run()
