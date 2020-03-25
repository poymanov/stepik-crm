from app import app
from flask import redirect, render_template, request
from app.forms import LoginForm
import app.services.users as users_service


@app.route('/')
def index():
    return redirect('admin')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        if users_service.login(form):

            next_url = request.args.get('next')

            if next_url:
                return redirect(next_url)
            else:
                return redirect('/')
        else:
            form.email.errors.append('Неверный email или пароль')
            return render_template('login.html', form=form)
    else:
        return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    if users_service.get_auth_user() is None:
        return redirect('/login')

    users_service.logout()
    return redirect('/login')
