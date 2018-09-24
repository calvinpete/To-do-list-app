# This file contains the code for managing a record of todo_lists

record = {}


def create_list(title):
    """
    This creates a todo_list with a title in a record of todo_lists
    :param title:
    :return record:
    """
    record[title] = []
    return record


def add_task(title, item):
    """
    This adds a to do list item
    :param title:
    :param item:
    :return record[title]:
    """
    record[title].append(item)
    return record[title]


def find_task(title, index):
    """
    This finds a specific item in the to do list
    :param title:
    :param index:
    :return record:
    """
    print(record[title][index])
    return record


def delete_task(title, index):
    """
    This deletes a specific to do list item
    :param title:
    :param index:
    :return record:
    """
    del record[title][index]
    print(record[title])
    return record


def edit_task(title, index, item):
    """
    This edits a specific to do list item
    :param title:
    :param index:
    :param item:
    :return record:
    """
    record[title][index] = item
    print(record[title])
    return record


def clear_task(title):
    """
    This clears the whole to do list
    :param title:
    :return record:
    """
    del record[title][:]
    return record
