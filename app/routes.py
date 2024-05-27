from app import app
from flask import redirect, render_template, request, flash
from .forms import TodoForm
from app import db


@app.route('/')
def index():
    return render_template('todos.html', title='Home')


@app.route("/new", methods=['GET', 'POST'])
def add_todo():
    if request.method == 'GET':
        form = TodoForm()
        return render_template('create.html', form=form)
    else:
        form = TodoForm(request.form)
        title = form.title.data
        description = form.description.data
        completed = form.completed.data
        todos = db["todos"]
        todos.insert_one(
            {'title': title, 'description': description, 'completed': completed})

        flash('Todo added successfully', 'success')
        return redirect('/')
