from flask import jsonify, request
from app import app
from app.tasks import Tasks

new_tasks = Tasks()


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
    if new_tasks.check_list(title):
        return jsonify({"message": "To do list already exists"}), 409
    new_tasks.new_list(title)
    return jsonify({"message": "To do list created successfully"}), 201


@app.route('/todo/api/v1/tasks/<title>', methods=['POST'])
def add_task(title):
    if "task" not in request.json:
        return jsonify({"message": "Invalid entry, please type the task"}), 400
    data = request.get_json()
    task = data["task"]
    if isinstance(task, int) or isinstance(task, float) or isinstance(task, list):
        return jsonify({"message": "Please enter a string"}), 400
    if not task:
        return jsonify({"message": "Task field is empty"}), 400
    if task.isspace():
        return jsonify({"message": "Task field is empty"}), 400
    if title in new_tasks.record:
        new_tasks.add_task(title, task)
        return jsonify({"message": "Task successfully added"}), 201
    else:
        return jsonify({"message": "To do list does not exist"}), 404


@app.route('/todo/api/v1/tasks/<title>/<int:task_id>', methods=['DELETE'])
def remove_task(title, task_id):
    if title not in new_tasks.record:
        return jsonify({"message": "The To do list does not exist"}), 404
    for index in range(len(new_tasks.record[title])-1):
        if task_id != index:
            continue
        else:
            new_tasks.delete_task(title, task_id)
            return jsonify({"message": "Task successfully deleted"})
    else:
        return jsonify({"message": "Task does not exist"})
