from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, EmailField, SelectField, SubmitField
from wtforms.validators import DataRequired, Optional

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY'


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
    if form.validate_on_submit():
        name = form.name.data
        text = form.text.data
        email = form.email.data
        rating = form.rating.data
        print(name, text, email, rating)
        return redirect('/')
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
