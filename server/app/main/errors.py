from flask import jsonify

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
