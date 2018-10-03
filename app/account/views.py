from flask import jsonify, request
from app import app
from app.accounts import Account

new_account = Account()


@app.errorhandler(400)
def bad_request(error):
    return jsonify({"message": "Invalid entry"})


@app.errorhandler(404)
def page_not_found(error):
    return jsonify({"message": "This page does not exist"})


@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({"message": "This method is not allowed for the requested URL"})


# @app.route('/todo/api/v1/auth/register', methods=['POST'])
# def register():
#
