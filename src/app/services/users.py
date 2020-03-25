from app.models import db, User
from werkzeug.security import check_password_hash
from flask import session


def login(form):
    user = db.session.query(User).filter(User.email == form.email.data).first()
    if user and check_password_hash(user.password, form.password.data):
        session['user'] = {'id': user.id, 'email': user.email}
        return True
    else:
        return False


def get_auth_user():
    if session.get('user'):
        return session['user']
    else:
        return None


def logout():
    session.pop('user')
