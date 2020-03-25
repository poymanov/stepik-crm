import click
from validate_email import validate_email
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import User
from werkzeug.security import generate_password_hash
import os

engine = create_engine(os.environ.get('SQLALCHEMY_DATABASE_URI'))
Session = sessionmaker(bind=engine)
session = Session()


def create():
    name = click.prompt('Введите имя пользователя', type=str)

    email = click.prompt('Введите email пользователя', type=str)

    if not validate_email(email):
        click.echo('Введен некорретный email')
        return

    existed_user = session.query(User).filter(User.email == email).first()

    if existed_user is not None:
        click.echo('Пользователь c указанным email уже существует')
        return

    password = click.prompt('Введите пароль пользователя', type=str, hide_input=True)
    password_confirmation = click.prompt('Введите пароль еще раз', type=str, hide_input=True)

    if password != password_confirmation:
        click.echo('Указанные пароли не совпадают')
        return

    user = User()
    user.name = name
    user.email = email
    user.password = generate_password_hash(password)
    session.add(user)
    session.commit()

    click.echo('Пользователь успешно создан')

if __name__ == '__main__':
    create()
