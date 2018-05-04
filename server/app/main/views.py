from flask import jsonify

from . import main
from ..models import TodoList, TodoItem


@main.route('/todo-list', methods=['GET'])
def index():
    todo_list = TodoList.query.all()
    todo_list = [l.json() for l in todo_list]
    return jsonify({'status': 'success', 'list': todo_list})
