from datetime import datetime

from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm

from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db = SQLAlchemy(app)


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    text = db.Column(db.Text, nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)


db.create_all()


class NewsForm(FlaskForm):
    title = StringField(
        'Название',
        validators=[DataRequired(message="Поле не должно быть пустым"),
                    Length(max=255, message='Введите заголовок длиной до 255 символов')]
    )
    text = TextAreaField(
        'Текст',
        validators=[DataRequired(message="Поле не должно быть пустым")])
    submit = SubmitField('Добавить')


@app.route('/')
def index():
    news_list = News.query.all()
    return render_template('index.html',
                           news=news_list)


@app.route('/news_detail/<int:id>')
def news_detail(id):
    news_detail = News.query.get(id)
    return render_template('news_detail.html',
                           news=news_detail)


@app.route('/add_news', methods=['GET', 'POST'])
def add_news():
    form = NewsForm()
    if form.validate_on_submit():
        news = News()
        news.title = form.title.data
        news.text = form.text.data
        db.session.add(news)
        db.session.commit()
        return redirect(url_for('news_detail', id=news.id))
    return render_template('add_news.html',
                           form=form)


if __name__ == '__main__':
    app.run(debug=True)
