from flask import jsonify, request
from app import app
from app.tasks import Tasks

task = Tasks()


@app.errorhandler(400)
def bad_request(error):
    return jsonify({"message": "Invalid entry"}), 400


@app.errorhandler(404)
def page_not_found(error):
    return jsonify({"message": "This page does not exist"}), 404


@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({"message": "This method is not allowed for the requested URL"}), 405


@app.route('/todo/api/v1/tasks', methods=['POST'])
def create_to_do_list():

    if "title" not in request.json:
        return jsonify({"message": "Invalid entry, please type the title"}), 400

    data = request.get_json()
    title = data['title']
    if isinstance(title, int) or isinstance(title, float) or isinstance(title, list):
        return jsonify({"message": "Please enter a string"})
    if not title:
        return jsonify({"message": "Title field is empty"}), 400
    if title.isspace():
        return jsonify({"message": "Title field is empty"}), 400
    if task.check_list(title):
        return jsonify({"message": "To do list already exists"}), 409
    task.new_list(title)
    return jsonify({"message": "To do list created successfully"}), 201


