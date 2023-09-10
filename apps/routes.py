from apps import app
from flask import render_template, flash, redirect, url_for
from apps.forms import LoginForm


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
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"Login requested for user{form.username.data}, remember_me{form.remember_me.data}, password{form.password.data}")
        # flash("All GOOD!")
        return redirect(url_for('index'))
    return render_template('login.html', title="Sign In", form=form)



# @app.route('/log')
# def log():
#     return render_template('base.html', title="LOG")

