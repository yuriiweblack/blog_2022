from apps import app
from flask import render_template
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


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title="Sign In", form=form)
