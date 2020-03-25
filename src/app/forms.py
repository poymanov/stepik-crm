from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField
from wtforms.validators import InputRequired, Length, Email


class MailerForm(FlaskForm):
    email = StringField('Кому', [InputRequired(), Length(min=5, message='Не менее 5 символов'),
                                 Email('Неверный формат электронного адреса')])
    subject = StringField('Тема', [InputRequired(), Length(min=3, message='Не менее 3 символов')])

    text = TextAreaField('Текст письма', [InputRequired(), Length(min=5, message='Не менее 5 символов')])


class LoginForm(FlaskForm):
    email = StringField('Email', [InputRequired(), Email('Неверный формат электронного адреса')])
    password = PasswordField('Пароль', [InputRequired()])
