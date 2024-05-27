from app import app
from flask import render_template

from .forms import TodoForm


@app.route('/')
def index():
    return render_template('todos.html', title='Home')


@app.route("/add_todo")
def add_todo():
    form = TodoForm()
    return render_template('create.html', form=form, )
