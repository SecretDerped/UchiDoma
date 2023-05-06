from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, EmailField, SelectField, SubmitField
from wtforms.validators import DataRequired, Optional

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db = SQLAlchemy(app)


class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(64))
    rating = db.Column(db.Integer)


with app.app_context():
    db.create_all()


class FeedbackForm(FlaskForm):
    name = StringField('Имя',
                       validators=[DataRequired(message="Поле не должно быть пустым")])
    text = TextAreaField('Текст отзыва',
                         validators=[DataRequired(message="Поле не должно быть пустым")])
    email = EmailField('Ваш email', validators=[Optional()])
    rating = SelectField('Ваша оценка?', choices=[1, 2, 3, 4, 5])
    submit = SubmitField('Добавить')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = FeedbackForm()
    feedbacks = Feedback.query.all()
    if form.validate_on_submit():
        feedback = Feedback(
            name=form.name.data,
            text=form.text.data,
            email=form.email.data,
            rating=form.rating.data
        )
        db.session.add(feedback)
        db.session.commit()
        return redirect('/')
    return render_template('index.html', form=form, feedbacks=feedbacks)


if __name__ == '__main__':
    app.run(debug=True)
