from flask import jsonify, make_response
import sqlalchemy.exc

from . import main
from ..exception import InvalidRequest


@main.errorhandler(InvalidRequest)
def handle_invalid_request(e):
    """handle customize exception

    :type e InvalidRequest
    :param e: exception param
    :return response: json exception
    """
    response = jsonify(e.json())
    response.status_code = e.status_code
    return response


@main.errorhandler(sqlalchemy.exc.IntegrityError)
def handle_unique_constraint(e):
    return make_response('todo-list content must be unique!', 400)
