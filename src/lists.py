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
    :return:
    """
    print(record[title][index])
    return record
