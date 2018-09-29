from flask import jsonify, request
from app import app
from app.tasks import Tasks

task = Tasks()


@app.route('/todo/api/v1/tasks', methods=['POST'])
def create_to_do_list():
    data = request.get_json()
    title = data['title']

    if not title:
        return jsonify({"message": "Title field is empty"}), 400
    if title.isspace():
        return jsonify({"message": "Title field is empty"}), 400
    if task.check_list(title):
        return jsonify({"message": "To do list already exists"}), 409
    task.new_list(title)
    return jsonify({"message": "To do list created successfully"}), 201


