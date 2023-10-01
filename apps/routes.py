from apps import app
from flask import render_template, flash, redirect, url_for
from apps.forms import LoginForm
from flask_login import current_user, login_user, logout_user

from apps.models import User


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Yurii'}
    posts = [
        {
            'author': {'username': 'David'},
            'body': 'Good sunny day!'
        },
        {
            'author': {'username': 'John'},
            'body': 'Bad foggy day!'
        }
    ]
    return render_template("index.html", title='Home page', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password!")
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        flash(f"User!!!! {user}!")
        return redirect(url_for('index'))

        # flash(f"User!!!! {user}!")
        # flash(f"Login requested for user{form.username.data}, remember_me{form.remember_me.data}, password{form.password.data}")
        # flash("All GOOD!")
        # return redirect(url_for('index'))
    return render_template('login.html', title="Sign In", form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

# @app.route('/log')
# def log():
#     return render_template('base.html', title="LOG")

