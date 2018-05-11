from flask import jsonify, request, make_response

from app import db
from app.exception import InvalidRequest
from . import main
from ..models import TodoList, TodoItem


@main.route('/todo-list', methods=['GET'])
def get_all_todo_list():
    todo_list = TodoList.query.all()
    todo_list = [l.json() for l in todo_list if not l.isDelete]
    return jsonify({'lists': todo_list}), 200


@main.route('/todo-list', methods=['POST'])
def post_a_todo_list():
    todo_list = TodoList(content='a new todo list')
    db.session.add(todo_list)
    db.session.commit()
    return make_response('Successfully created a new todo-list!', 201)


@main.route('/todo-list/<list_id>', methods=['PUT'])
def update_a_specify_todo_list(list_id: int):
    todo_list = TodoList.query.filter_by(id=list_id).first()  # type: TodoList
    if todo_list is None:
        raise InvalidRequest('todo-list id is invalid!')
    if not request.json:
        raise InvalidRequest('Content-Type must be JSON!')
    todo_list.content = request.json.get('content') or todo_list.content
    todo_list.isDelete = request.json.get('isDelete')
    todo_list.locked = request.json.get('locked')
    return make_response('Successfully updated a todo list', 200)


@main.route('/todo-list/<list_id>/todo-item', methods=['GET'])
def get_all_todo_items(list_id: int):
    todo_list = TodoList.query.filter_by(id=list_id).first()  # type: TodoList
    if todo_list is None:
        raise InvalidRequest('todo-list id is invalid!')
    items = todo_list.items
    items = [item.json() for item in items]
    # return jsonify({'items': items}), 200
    json = todo_list.json()
    json['items'] = items
    return jsonify(json), 200


@main.route('/todo-list/<list_id>/todo-item', methods=['POST'])
def create_a_todo_item_of_specify_todo_list(list_id):
    import datetime

    if not request.json:
        raise InvalidRequest('Require JSON format todo-item POST!')
    todo_list = TodoList.query.get(list_id)  # type: TodoList
    if todo_list is None:
        raise InvalidRequest('todo-list id is invalid!')
    item = TodoItem(content=request.json.get('content'), date=datetime.datetime.now().date())
    item.list_id = todo_list.id
    db.session.add(item)
    db.session.commit()
    return make_response('Successfully created a todo item!', 201)


@main.route('/todo-list/<list_id>/todo-item/<item_id>', methods=['PUT'])
def update_a_specify_todo_item(list_id, item_id):
    item = TodoItem.query.filter_by(id=item_id).first() # type: TodoItem
    if not item:
        raise InvalidRequest('item id is invalid!')
    item.content = request.json.get('content') or item.content
    item.isDone = request.json.get('isDone')
    print(request.json.get('isDone'))
    return make_response('Successfully updated a item', 200)
