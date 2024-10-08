from bson import ObjectId
import requests
from app import app
from flask import redirect, render_template, request, flash, url_for
from .forms import TodoForm
from app import db


def api_request(method, endpoint, json=None):
    url = request.host_url.strip('/') + '/api' + endpoint
    headers = {'Content-Type': 'application/json'}
    response = requests.request(method, url, headers=headers, json=json)
    return response.json(), response.status_code


@app.route('/')
def home():
    todos = []
    for td in db["todos"].find().sort('completed'):
        td["_id"] = str(td["_id"])
        todo = {
            'title': td['title'],
            'description': td['description'],
            'completed': td['completed'],
            '_id': td['_id']
        }
        todos.append(todo)

    return render_template('todos.html', title='Home', todos=todos)


@app.route("/new", methods=['GET', 'POST'])
def add_todo():
    if request.method == 'GET':
        form = TodoForm()
        return render_template('upsert.html', title='Create New Todo', form=form)
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


@app.route("/todo/<string:_id>", methods=["GET", "POST"])
def update(_id):
    if request.method == "POST":
        form = TodoForm(request.form)

        if not form.validate():
            flash('All fields are required', 'danger')
            return redirect('/todo/' + _id)

        db["todos"].update_one({'_id': ObjectId(_id)}, {
            '$set': {'title': form.title.data, 'description': form.description.data, 'completed': form.completed.data}})
        flash('Todo updated successfully', 'success')
        return redirect('/')
    else:
        form = TodoForm()
        todo = db["todos"].find_one({'_id': ObjectId(_id)})

        if not todo:
            return render_template('404.html'), 404

        form.title.data = todo.get('title', None)
        form.description.data = todo.get('description', None)
        form.completed.data = todo.get('completed', None)

        return render_template('upsert.html', title='Update Todo', form=form)


@app.route("/delete/<string:_id>")
def delete(_id):
    db["todos"].delete_one({'_id': ObjectId(_id)})
    flash('Todo deleted successfully', 'success')
    return redirect('/')


@app.route("/api/todos", methods=["GET", "POST"])
def get_post():
    if request.method == "GET":
        todos = []
        for td in db["todos"].find().sort('completed'):
            td["_id"] = str(td["_id"])
            todo = {
                'title': td['title'],
                'description': td['description'],
                'completed': td['completed'],
                '_id': td['_id']
            }
            todos.append(todo)

        return {'todos': todos}, 200

    elif request.method == "POST":
        data = request.json
        if not data:
            return {'error': 'Data is required'}, 400

        title = data.get('title', None)
        description = data.get('description', None)
        completed = data.get('completed', None)

        if not title:
            return {'error': 'Title is required'}, 400

        db["todos"].insert_one(
            {'title': title, 'description': description, 'completed': completed})
        return {'message': 'Todo added successfully'}, 201
    else:
        return {'error': 'Invalid request method'}, 405


@app.route("/api/todos/<string:_id>", methods=["GET", "PUT", "DELETE"])
def get_update_delete(_id):
    if request.method == "GET":
        todo = db["todos"].find_one({'_id': ObjectId(_id)})
        if not todo:
            return {'error': 'Todo not found'}, 404

        todo["_id"] = str(todo["_id"])
        return {'todo': todo}, 200

    elif request.method == "PUT":
        data = request.json
        if not data:
            return {'error': 'Data is required'}, 400

        db["todos"].update_one({'_id': ObjectId(_id)}, {
            '$set': {'title': data.get('title', None), 'description': data.get('description', None), 'completed': data.get('completed', None)}})
        return {'message': 'Todo updated successfully'}, 200

    elif request.method == "DELETE":
        db["todos"].delete_one({'_id': ObjectId(_id)})
        return {'message': 'Todo deleted successfully'}, 200
    else:
        return {'error': 'Invalid request method'}, 405
