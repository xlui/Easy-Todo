from flask import jsonify, request, abort

from app.exception import InvalidRequest
from . import main
from ..models import TodoList, TodoItem


@main.route('/todo-list', methods=['GET'])
def get_all_todo_list():
    todo_list = TodoList.query.all()
    todo_list = [l.json() for l in todo_list]
    return jsonify({'status': 'success', 'list': todo_list})


@main.route('/todo-list', methods=['POST'])
def post_a_todo_list():
    if not request.json:
        abort(400)


@main.route('/t')
def t():
    raise InvalidRequest('This is a test exception', status_code=401)
